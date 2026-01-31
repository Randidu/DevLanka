// Smart API URL Detection
let API_BASE = '';
const hostname = window.location.hostname;
const isLocalhost = hostname === '127.0.0.1' || hostname === 'localhost';

if (isLocalhost) {
    // Running locally - use local backend
    API_BASE = 'http://127.0.0.1:8000/api';
    console.log("🔧 Development Mode: using local backend at " + API_BASE);
} else {
    // Dynamic Production Mode (Render / Custom Domain)
    // This will automatically pick up https://devlanka-1.onrender.com or any other domain
    // If you are on the same domain as the backend, relative path '/api' is best,
    // but window.location.origin + '/api' is safer for absolute URL needs.

    if (hostname.includes('onrender.com')) {
        API_BASE = '/api'; // Use relative path for Render internal routing
        console.log("🚀 Production Mode (Render): using relative paths");
    } else {
        API_BASE = window.location.origin + '/api';
        console.log("☁️ Production Mode: using backend at " + API_BASE);
    }
}

// For Authentication URL (No /api suffix)
let AUTH_BASE = API_BASE.replace('/api', '');
