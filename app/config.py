import os
import firebase_admin
from firebase_admin import credentials, auth, firestore, storage


cred = credentials.Certificate("app/firebase_config.json")
firebase_admin.initialize_app(cred, {
    'storageBucket': 'f1-management-ded6e6.appspot.com'
})


db = firestore.client()


FIREBASE_API_KEY = os.getenv("FIREBASE_API_KEY", "AIzaSyCacsel7VnAAApI3doWvGNzvE7ztedrvYo")
firebase.initializeApp(firebaseConfig);

firebase.auth().onAuthStateChanged((user) => {
    if (user) {
        console.log("User is logged in:", user.email);
        user.getIdToken().then((token) => {
            document.cookie = `firebase_token=${token}`;
        });
    } else {
        console.log("No user detected, redirecting to login...");
        window.location.href = "/login";
    }
});
