self.addEventListener('install', function(event) {
    console.log('Admin Service Worker Installed');
});

self.addEventListener('fetch', function(event) {
    // Basic service worker (no caching yet)
});
