document.addEventListener('DOMContentLoaded', () => {
    // Sayfa açılınca mevcut sayıyı getir
    fetch('/api/get-likes')
        .then(res => res.json())
        .then(data => {
            document.getElementById('like-count').innerText = data.likes;
            updateHeartVisual(data.likes > 0);
        });
});

async function sendLike() {
    const heart = document.getElementById('heart-btn');
    
    // Tıklama animasyonu ekle
    heart.classList.add('pump');
    
    // Animasyon bitince class'ı kaldır (tekrar tıklanabilsin diye)
    setTimeout(() => {
        heart.classList.remove('pump');
    }, 400);

    try {
        // Backend'e "Beğendim" de
        const response = await fetch('/api/like', { method: 'POST' });
        const data = await response.json();
        
        // Sayıyı güncelle
        document.getElementById('like-count').innerText = data.likes;
        updateHeartVisual(true);
        
    } catch (error) {
        console.error("Hata:", error);
    }
}

function updateHeartVisual(isActive) {
    const heart = document.getElementById('heart-btn');
    if (isActive) {
        heart.style.color = "#ff4d4d";
        heart.style.textShadow = "0 0 20px #ff0000";
    }
}
