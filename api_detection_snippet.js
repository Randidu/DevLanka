/**
 * SMART API URL DETECTION - QUICK REFERENCE
 * Copy this code snippet to any new HTML file that needs API access
 */

// Smart API URL Detection
let API_BASE = '';
const hostname = window.location.hostname;
const isLocalhost = hostname === '127.0.0.1' || hostname === 'localhost';

if (isLocalhost) {
    // Running locally - use local backend
    API_BASE = 'http://127.0.0.1:8000/api';
    console.log("🔧 Development Mode: using local backend at " + API_BASE);
} else if (hostname.includes('onrender.com')) {
    // Running on Render - use relative paths
    API_BASE = '/api';
    console.log("🚀 Production Mode (Render): using relative paths");
} else {
    // Fallback to Render for any other domain
    API_BASE = 'https://devlanka-hub.onrender.com/api';
    console.log("☁️ Fallback: using Render backend at " + API_BASE);
}

/**
 * USAGE EXAMPLES:
 * 
 * 1. Fetch data from API:
 *    const response = await fetch(`${API_BASE}/resources/`);
 * 
 * 2. POST data to API:
 *    const response = await fetch(`${API_BASE}/news/`, {
 *        method: 'POST',
 *        headers: { 'Content-Type': 'application/json' },
 *        body: JSON.stringify(data)
 *    });
 * 
 * 3. With authentication:
 *    const token = localStorage.getItem('access_token');
 *    const response = await fetch(`${API_BASE}/auth/me`, {
 *        headers: { 'Authorization': `Bearer ${token}` }
 *    });
 */

/**
 * FOR AUTH ENDPOINTS (login, register, etc.):
 * Use AUTH_BASE instead of API_BASE
 */

// For auth endpoints only
let AUTH_BASE = '';
if (isLocalhost) {
    AUTH_BASE = 'http://127.0.0.1:8000';
    console.log("🔧 Development Mode: using local backend");
} else if (hostname.includes('onrender.com')) {
    AUTH_BASE = '';
    console.log("🚀 Production Mode (Render)");
} else {
    AUTH_BASE = 'https://devlanka-hub.onrender.com';
    console.log("☁️ Fallback: using Render backend");
}

// Usage: fetch(`${AUTH_BASE}/auth/login`, {...})
