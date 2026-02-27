#!/usr/bin/env python3
"""
Generate plots for the "Physics Wins: Starlink Jamming" blog post.

Creates:
1. J/S vs Distance plot
2. Countermeasure comparison bar chart
3. Link budget waterfall chart
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from pathlib import Path

# Set style for clean, professional plots
plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.size'] = 11
plt.rcParams['axes.labelsize'] = 12
plt.rcParams['axes.titlesize'] = 14
plt.rcParams['figure.facecolor'] = 'white'
plt.rcParams['axes.facecolor'] = 'white'
plt.rcParams['savefig.facecolor'] = 'white'
plt.rcParams['savefig.edgecolor'] = 'white'

# Output directory
OUTPUT_DIR = Path(__file__).parent.parent / "public" / "images" / "physics-wins-jamming"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Constants for calculations
SATELLITE_ALTITUDE_M = 550_000  # 550 km
FREQUENCY_HZ = 12e9  # 12 GHz (Ku-band)
C = 3e8  # Speed of light

# Jammer parameters
JAMMER_POWER_DBW = 40  # 10 kW = +40 dBW
JAMMER_ANTENNA_GAIN_DBI = 10
JAMMER_EIRP_DBW = JAMMER_POWER_DBW + JAMMER_ANTENNA_GAIN_DBI  # 50 dBW

# Satellite parameters
SATELLITE_EIRP_DBW = 35
RECEIVER_GAIN_DBI = 30

# Countermeasure gains (dB)
COUNTERMEASURES = {
    'Adaptive\nBeamforming': 40,
    'Frequency\nHopping': 20,
    'Forward Error\nCorrection': 10,
}
TOTAL_COUNTERMEASURE_DB = sum(COUNTERMEASURES.values())


def free_space_path_loss_db(distance_m, frequency_hz):
    """Calculate free space path loss in dB."""
    wavelength = C / frequency_hz
    fspl = (4 * np.pi * distance_m / wavelength) ** 2
    return 10 * np.log10(fspl)


def calculate_js_ratio(jammer_distance_m):
    """Calculate J/S ratio for given jammer distance."""
    # Satellite path loss (fixed)
    fspl_satellite = free_space_path_loss_db(SATELLITE_ALTITUDE_M, FREQUENCY_HZ)
    p_satellite = SATELLITE_EIRP_DBW - fspl_satellite + RECEIVER_GAIN_DBI

    # Jammer path loss (variable with distance)
    fspl_jammer = free_space_path_loss_db(jammer_distance_m, FREQUENCY_HZ)
    p_jammer = JAMMER_EIRP_DBW - fspl_jammer + RECEIVER_GAIN_DBI

    # J/S ratio
    js_ratio = p_jammer - p_satellite
    return js_ratio


def plot_js_vs_distance():
    """Plot J/S ratio vs jammer distance with countermeasure threshold."""
    fig, ax = plt.subplots(figsize=(10, 6))

    # Distance range: 10m to 100km (log scale)
    distances = np.logspace(1, 5, 500)  # 10m to 100km
    js_ratios = [calculate_js_ratio(d) for d in distances]

    # Plot J/S ratio
    ax.semilogx(distances, js_ratios, 'b-', linewidth=2.5, label='J/S Ratio (raw)')

    # Plot effective J/S after countermeasures
    js_after_cm = [js - TOTAL_COUNTERMEASURE_DB for js in js_ratios]
    ax.semilogx(distances, js_after_cm, 'g--', linewidth=2.5,
                label=f'J/S after countermeasures (−{TOTAL_COUNTERMEASURE_DB} dB)')

    # Threshold line at 0 dB (where jammer = signal)
    ax.axhline(y=0, color='red', linestyle='-', linewidth=2, label='Link failure threshold (J/S = 0 dB)')

    # Find crossover points
    # Raw J/S = 0 crossover (very far, beyond our range typically)
    # After CM J/S = 0 crossover
    for i, (d, js) in enumerate(zip(distances[:-1], js_after_cm[:-1])):
        if js_after_cm[i] > 0 and js_after_cm[i+1] <= 0:
            crossover_distance = d
            ax.axvline(x=crossover_distance, color='green', linestyle=':', alpha=0.7)
            ax.annotate(f'Countermeasures effective\nbeyond ~{crossover_distance/1000:.1f} km',
                       xy=(crossover_distance, 5), fontsize=10,
                       ha='left', va='bottom',
                       bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.8))
            break

    # Mark key distances
    key_distances = [100, 1000, 5000, 10000]
    for d in key_distances:
        js = calculate_js_ratio(d)
        ax.plot(d, js, 'bo', markersize=8)
        ax.annotate(f'{d}m\n{js:.0f} dB', xy=(d, js), xytext=(d*1.3, js+5),
                   fontsize=9, ha='left')

    # Shade regions
    ax.fill_between(distances, js_after_cm, 0, where=[js > 0 for js in js_after_cm],
                    color='red', alpha=0.15, label='Jammer wins (even with countermeasures)')
    ax.fill_between(distances, js_after_cm, 0, where=[js <= 0 for js in js_after_cm],
                    color='green', alpha=0.15, label='Link survives')

    ax.set_xlabel('Jammer Distance (meters)', fontsize=12)
    ax.set_ylabel('Jamming-to-Signal Ratio (dB)', fontsize=12)
    ax.set_title('J/S Ratio vs. Jammer Distance\n(10 kW jammer, Starlink at 550 km, 12 GHz)', fontsize=14)
    ax.legend(loc='upper right', fontsize=9)
    ax.set_xlim(10, 100000)
    ax.set_ylim(-20, 120)
    ax.grid(True, alpha=0.3)

    # Add annotation explaining the physics
    ax.text(50, 100, '"Physics wins"\nzone', fontsize=12, fontweight='bold',
            color='darkred', ha='center', va='center',
            bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.9))

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'js_vs_distance.png', dpi=150, bbox_inches='tight')
    plt.close()
    print(f"Saved: {OUTPUT_DIR / 'js_vs_distance.png'}")


def plot_countermeasure_comparison():
    """Bar chart comparing countermeasure effectiveness."""
    fig, ax = plt.subplots(figsize=(10, 6))

    # Data
    categories = list(COUNTERMEASURES.keys())
    values = list(COUNTERMEASURES.values())
    colors = ['#2ecc71', '#3498db', '#9b59b6']

    # Create bars
    bars = ax.bar(categories, values, color=colors, edgecolor='black', linewidth=1.5)

    # Add value labels on bars
    for bar, val in zip(bars, values):
        height = bar.get_height()
        ax.annotate(f'{val} dB',
                   xy=(bar.get_x() + bar.get_width() / 2, height),
                   xytext=(0, 5),
                   textcoords="offset points",
                   ha='center', va='bottom', fontsize=14, fontweight='bold')

    # Add total line
    total = sum(values)
    ax.axhline(y=total, color='red', linestyle='--', linewidth=2, label=f'Combined total: {total} dB')

    # Add jammer advantage reference
    jammer_advantage = 90
    ax.axhline(y=jammer_advantage, color='darkred', linestyle='-', linewidth=2.5,
               label=f'Jammer advantage at 100m: ~{jammer_advantage} dB')

    # Shade the gap
    ax.fill_between([-0.5, 2.5], total, jammer_advantage, color='red', alpha=0.2)
    ax.annotate(f'Deficit: {jammer_advantage - total} dB\n(Jammer wins)',
               xy=(2.3, (total + jammer_advantage)/2),
               fontsize=11, ha='center', va='center', fontweight='bold',
               bbox=dict(boxstyle='round', facecolor='mistyrose', alpha=0.9))

    ax.set_ylabel('Jamming Rejection (dB)', fontsize=12)
    ax.set_title('Software Countermeasure Effectiveness\nvs. Near-Field High-Power Jammer', fontsize=14)
    ax.legend(loc='upper left', fontsize=10)
    ax.set_ylim(0, 110)
    ax.set_xlim(-0.5, 2.5)

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'countermeasure_comparison.png', dpi=150, bbox_inches='tight')
    plt.close()
    print(f"Saved: {OUTPUT_DIR / 'countermeasure_comparison.png'}")


def plot_link_budget_waterfall():
    """Waterfall chart showing satellite vs jammer link budgets."""
    fig, ax = plt.subplots(figsize=(12, 7))

    # Satellite link budget
    sat_stages = ['Satellite\nEIRP', 'Path Loss\n(550 km)', 'Receiver\nGain', 'Received\nPower']
    sat_values = [35, -168.85, 30, -103.85]
    sat_cumulative = [35, 35-168.85, 35-168.85+30, -103.85]

    # Jammer link budget
    jam_stages = ['Jammer\nEIRP', 'Path Loss\n(100 m)', 'Receiver\nGain', 'Received\nPower']
    jam_values = [50, -94.05, 30, -14.05]
    jam_cumulative = [50, 50-94.05, 50-94.05+30, -14.05]

    # X positions
    x_sat = np.arange(len(sat_stages))
    x_jam = np.arange(len(jam_stages)) + 5  # Offset for jammer

    # Plot satellite waterfall
    colors_sat = ['green' if v >= 0 else 'red' for v in [35, -168.85, 30, 0]]
    for i, (stage, cum, val) in enumerate(zip(sat_stages, sat_cumulative, sat_values)):
        if i == 0:
            ax.bar(x_sat[i], val, color='#27ae60', edgecolor='black', linewidth=1.5)
        elif i == len(sat_stages) - 1:
            ax.bar(x_sat[i], cum, color='#27ae60', edgecolor='black', linewidth=1.5)
        else:
            bottom = sat_cumulative[i-1] if i > 0 else 0
            color = '#27ae60' if val > 0 else '#e74c3c'
            ax.bar(x_sat[i], val, bottom=bottom, color=color, edgecolor='black', linewidth=1.5)
        ax.text(x_sat[i], sat_cumulative[i] + 3, f'{sat_cumulative[i]:.1f}',
                ha='center', fontsize=10, fontweight='bold')

    # Plot jammer waterfall
    for i, (stage, cum, val) in enumerate(zip(jam_stages, jam_cumulative, jam_values)):
        if i == 0:
            ax.bar(x_jam[i], val, color='#e74c3c', edgecolor='black', linewidth=1.5)
        elif i == len(jam_stages) - 1:
            ax.bar(x_jam[i], cum, color='#e74c3c', edgecolor='black', linewidth=1.5)
        else:
            bottom = jam_cumulative[i-1] if i > 0 else 0
            color = '#e74c3c' if val < 0 else '#f39c12'
            ax.bar(x_jam[i], val, bottom=bottom, color=color, edgecolor='black', linewidth=1.5)
        ax.text(x_jam[i], jam_cumulative[i] + 3, f'{jam_cumulative[i]:.1f}',
                ha='center', fontsize=10, fontweight='bold')

    # Draw comparison arrow
    ax.annotate('', xy=(8.5, -14.05), xytext=(8.5, -103.85),
                arrowprops=dict(arrowstyle='<->', color='purple', lw=3))
    ax.text(9, -60, f'J/S = 89.8 dB\n(Jammer advantage)',
            fontsize=12, fontweight='bold', color='purple',
            bbox=dict(boxstyle='round', facecolor='lavender', alpha=0.9))

    # Labels
    all_stages = list(sat_stages) + [''] + list(jam_stages)
    ax.set_xticks(list(x_sat) + [4] + list(x_jam))
    ax.set_xticklabels(all_stages, fontsize=10)

    # Add section labels
    ax.text(1.5, 60, 'SATELLITE LINK\n(550 km away)', ha='center', fontsize=12,
            fontweight='bold', color='#27ae60',
            bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.7))
    ax.text(6.5, 60, 'JAMMER LINK\n(100 m away)', ha='center', fontsize=12,
            fontweight='bold', color='#c0392b',
            bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7))

    ax.set_ylabel('Power Level (dBW)', fontsize=12)
    ax.set_title('Link Budget Comparison: Satellite Signal vs. Ground Jammer\n(12 GHz Ku-band)', fontsize=14)
    ax.axhline(y=0, color='black', linestyle='-', linewidth=0.5)
    ax.set_ylim(-180, 80)
    ax.grid(True, axis='y', alpha=0.3)

    # Legend
    legend_elements = [
        mpatches.Patch(facecolor='#27ae60', edgecolor='black', label='Satellite signal'),
        mpatches.Patch(facecolor='#e74c3c', edgecolor='black', label='Jammer signal'),
        mpatches.Patch(facecolor='#f39c12', edgecolor='black', label='Gain'),
    ]
    ax.legend(handles=legend_elements, loc='lower left', fontsize=10)

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'link_budget_waterfall.png', dpi=150, bbox_inches='tight')
    plt.close()
    print(f"Saved: {OUTPUT_DIR / 'link_budget_waterfall.png'}")


def plot_inverse_square_law():
    """Plot showing inverse square law power decay for satellite vs jammer."""
    fig, ax = plt.subplots(figsize=(10, 6))

    # Distance range
    distances = np.logspace(1, 6, 500)  # 10m to 1000km

    # Received power (normalized) - inverse square law
    # P_received ∝ 1/d²
    # In dB: P_received = P_transmitted - 20*log10(d) + const

    # Satellite starts at 550km, we show power as it would be at various distances
    satellite_power_550km = -103.85  # dBW at 550km
    # If satellite were at different distances (hypothetically)
    satellite_at_distances = satellite_power_550km + 20*np.log10(550000/distances)

    # Jammer at various distances (actual scenario)
    jammer_power_ref = -14.05  # dBW at 100m
    jammer_at_distances = jammer_power_ref + 20*np.log10(100/distances)

    ax.semilogx(distances/1000, satellite_at_distances, 'b-', linewidth=2.5,
                label='Satellite signal (fixed at 550 km)')
    ax.semilogx(distances/1000, jammer_at_distances, 'r-', linewidth=2.5,
                label='Jammer signal (varying distance)')

    # Mark actual positions
    ax.axvline(x=550, color='blue', linestyle='--', alpha=0.5)
    ax.axvline(x=0.1, color='red', linestyle='--', alpha=0.5)

    ax.plot(550, satellite_power_550km, 'bo', markersize=12, zorder=5)
    ax.annotate('Starlink satellite\n550 km, -104 dBW', xy=(550, satellite_power_550km),
               xytext=(100, -80), fontsize=10,
               arrowprops=dict(arrowstyle='->', color='blue'),
               bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.8))

    ax.plot(0.1, jammer_power_ref, 'ro', markersize=12, zorder=5)
    ax.annotate('Jammer\n100 m, -14 dBW', xy=(0.1, jammer_power_ref),
               xytext=(0.3, 10), fontsize=10,
               arrowprops=dict(arrowstyle='->', color='red'),
               bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

    # Find crossover
    crossover_idx = np.argmin(np.abs(satellite_at_distances - jammer_at_distances))
    crossover_dist = distances[crossover_idx]/1000
    crossover_power = satellite_at_distances[crossover_idx]

    ax.set_xlabel('Distance (km)', fontsize=12)
    ax.set_ylabel('Received Power (dBW)', fontsize=12)
    ax.set_title('Inverse Square Law: Why Proximity Dominates\n(Power decreases with distance²)', fontsize=14)
    ax.legend(loc='lower left', fontsize=10)
    ax.grid(True, alpha=0.3)
    ax.set_xlim(0.01, 1000)
    ax.set_ylim(-150, 50)

    # Add annotation about 6dB per doubling
    ax.text(1, -130, 'Every doubling of distance\n= 6 dB power reduction',
            fontsize=10, ha='center',
            bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.9))

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'inverse_square_law.png', dpi=150, bbox_inches='tight')
    plt.close()
    print(f"Saved: {OUTPUT_DIR / 'inverse_square_law.png'}")


if __name__ == '__main__':
    print("Generating plots for 'Physics Wins' blog post...")
    plot_js_vs_distance()
    plot_countermeasure_comparison()
    plot_link_budget_waterfall()
    plot_inverse_square_law()
    print("\nAll plots generated successfully!")
