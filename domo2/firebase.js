// ── DOMO Firebase Config ──────────────────────────────
import { initializeApp } from "https://www.gstatic.com/firebasejs/11.0.0/firebase-app.js";
import { getAuth, onAuthStateChanged, signOut } from "https://www.gstatic.com/firebasejs/11.0.0/firebase-auth.js";
import { getFirestore, doc, setDoc, addDoc, collection, serverTimestamp } from "https://www.gstatic.com/firebasejs/11.0.0/firebase-firestore.js";

const firebaseConfig = {
  apiKey: "AIzaSyA6_5oWBRKZLnZhTsjtfepm2NleAEEsrPA",
  authDomain: "domo-8cfe1.firebaseapp.com",
  projectId: "domo-8cfe1",
  storageBucket: "domo-8cfe1.firebasestorage.app",
  messagingSenderId: "47790816831",
  appId: "1:47790816831:web:0a92e160fc595d5a9c428a"
};

const app = initializeApp(firebaseConfig);
export const auth = getAuth(app);
export const db = getFirestore(app);

// ── Track page view ───────────────────────────────────
export async function trackPageView(pageName, productSlug) {
  onAuthStateChanged(auth, async (user) => {
    if (!user) return;
    try {
      await addDoc(collection(db, "users", user.uid, "pageViews"), {
        page: pageName,
        slug: productSlug || null,
        timestamp: serverTimestamp(),
      });
    } catch(e) {}
  });
}

// ── Save to wishlist ──────────────────────────────────
export async function saveToWishlist(product) {
  const user = auth.currentUser;
  if (!user) { window.location.href = 'login.html'; return; }
  try {
    await setDoc(doc(db, "users", user.uid, "wishlist", product.slug), {
      ...product,
      savedAt: serverTimestamp(),
    });
  } catch(e) {}
}

// ── Track add to cart ─────────────────────────────────
export async function trackCartAdd(product) {
  const user = auth.currentUser;
  if (!user) return;
  try {
    await addDoc(collection(db, "users", user.uid, "cartEvents"), {
      ...product,
      action: 'add',
      timestamp: serverTimestamp(),
    });
  } catch(e) {}
}

// ── Save message (paper boat etc) ────────────────────
export async function saveMessage(text, source) {
  const user = auth.currentUser;
  if (!user) return;
  try {
    await addDoc(collection(db, "users", user.uid, "messages"), {
      text,
      source,
      timestamp: serverTimestamp(),
    });
  } catch(e) {}
}

// ── Save order ────────────────────────────────────────
export async function saveOrder(orderData) {
  const user = auth.currentUser;
  if (!user) return;
  try {
    await addDoc(collection(db, "users", user.uid, "orders"), {
      ...orderData,
      timestamp: serverTimestamp(),
    });
  } catch(e) {}
}

// ── Render nav avatar on any page ────────────────────
export function initNavAuth() {
  onAuthStateChanged(auth, (user) => {
    const loginLink = document.getElementById('navLoginLink');
    const avatarWrap = document.getElementById('navAvatar');
    if (!loginLink && !avatarWrap) return;

    if (user) {
      if (loginLink) loginLink.style.display = 'none';
      if (avatarWrap) {
        const initial = (user.displayName || user.email || '?')[0].toUpperCase();
        avatarWrap.style.display = 'flex';
        avatarWrap.querySelector('.nav-avatar-initial').textContent = initial;
        avatarWrap.querySelector('.nav-avatar-name').textContent = user.displayName || user.email.split('@')[0];
        avatarWrap.querySelector('.nav-avatar-email').textContent = user.email;
      }
    } else {
      if (loginLink) loginLink.style.display = '';
      if (avatarWrap) avatarWrap.style.display = 'none';
    }
  });
}

export { onAuthStateChanged, signOut };
