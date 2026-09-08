/* Dino Odkrywca – service worker: praca offline.
   index.html i manifest: najpierw sieć (żeby aktualizacje wchodziły od razu), potem cache.
   assets/ i ikony: najpierw cache (obrazki się nie zmieniają), potem sieć. */
const CACHE = 'dino-v3';
const CORE = ['./', './index.html', './manifest.json', './icons/icon-192.png', './icons/icon-512.png', './fonts/fredoka-latin-500-normal.woff2', './fonts/fredoka-latin-600-normal.woff2', './fonts/fredoka-latin-700-normal.woff2', './fonts/fredoka-latin-ext-500-normal.woff2', './fonts/fredoka-latin-ext-600-normal.woff2', './fonts/fredoka-latin-ext-700-normal.woff2'];
self.addEventListener('install', e => { e.waitUntil(caches.open(CACHE).then(c => c.addAll(CORE)).then(() => self.skipWaiting())); });
self.addEventListener('activate', e => { e.waitUntil(caches.keys().then(ks => Promise.all(ks.filter(k => k !== CACHE).map(k => caches.delete(k)))).then(() => self.clients.claim())); });
self.addEventListener('fetch', e => {
  const url = new URL(e.request.url);
  if(e.request.method !== 'GET' || url.origin !== location.origin) return;
  const isAsset = /\/(assets|icons|fonts)\//.test(url.pathname);
  if(isAsset){
    e.respondWith(caches.match(e.request).then(hit => hit || fetch(e.request).then(res => { if(res.ok){ const copy = res.clone(); caches.open(CACHE).then(c => c.put(e.request, copy)); } return res; }).catch(() => hit)));
  } else {
    e.respondWith(fetch(e.request).then(res => { if(res.ok){ const copy = res.clone(); caches.open(CACHE).then(c => c.put(e.request, copy)); } return res; }).catch(() => caches.match(e.request).then(hit => hit || caches.match('./index.html'))));
  }
});
