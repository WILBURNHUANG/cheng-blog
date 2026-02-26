import type { VercelRequest, VercelResponse } from '@vercel/node';

// Simple email validation regex
const EMAIL_REGEX = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

export default async function handler(req: VercelRequest, res: VercelResponse) {
  // Only allow POST requests
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  const { email } = req.body;

  // Validate email
  if (!email || typeof email !== 'string') {
    return res.status(400).json({ error: 'Email is required' });
  }

  if (!EMAIL_REGEX.test(email)) {
    return res.status(400).json({ error: 'Please enter a valid email address' });
  }

  // Get Mailchimp credentials from environment
  const API_KEY = process.env.MAILCHIMP_API_KEY;
  const AUDIENCE_ID = process.env.MAILCHIMP_AUDIENCE_ID;
  const SERVER = process.env.MAILCHIMP_SERVER;

  if (!API_KEY || !AUDIENCE_ID || !SERVER) {
    console.error('Missing Mailchimp configuration');
    return res.status(500).json({ error: 'Newsletter service is not configured' });
  }

  try {
    const response = await fetch(
      `https://${SERVER}.api.mailchimp.com/3.0/lists/${AUDIENCE_ID}/members`,
      {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          Authorization: `Basic ${Buffer.from(`anystring:${API_KEY}`).toString('base64')}`,
        },
        body: JSON.stringify({
          email_address: email,
          status: 'subscribed',
        }),
      }
    );

    const data = await response.json();

    if (response.ok) {
      return res.status(200).json({ message: 'Thanks for subscribing!' });
    }

    // Handle Mailchimp-specific errors
    if (data.title === 'Member Exists') {
      return res.status(400).json({ error: 'You are already subscribed!' });
    }

    if (data.title === 'Invalid Resource') {
      return res.status(400).json({ error: 'Please enter a valid email address' });
    }

    console.error('Mailchimp error:', JSON.stringify(data));
    // Return detailed error for debugging
    return res.status(500).json({
      error: data.detail || data.title || 'Failed to subscribe. Please try again.'
    });
  } catch (error) {
    console.error('Subscribe error:', error);
    return res.status(500).json({
      error: 'Failed to subscribe. Please try again.',
      debug: process.env.NODE_ENV === 'development' ? String(error) : undefined
    });
  }
}
