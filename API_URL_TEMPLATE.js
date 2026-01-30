// Smart API URL Detection - Use this in all HTML files
// Copy this code block to replace the API_BASE initialization

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

// For auth endpoints (without /api suffix):
const AUTH_BASE = API_BASE.replace('/api', '');
// Use: fetch(`${AUTH_BASE}/auth/login`, ...)
