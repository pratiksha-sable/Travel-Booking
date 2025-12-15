// Scroll to Packages section from hero button
function scrollToPackages() {
  document.getElementById('packages').scrollIntoView({ behavior: 'smooth' });
}

// Open booking modal with package name
function openBookingModal(packageName) {
  const modal = document.getElementById('bookingModal');
  const title = document.getElementById('modalTitle');
  title.textContent = `Book: ${packageName}`;
  modal.style.display = 'block';
}

// Close modal
function closeModal() {
  document.getElementById('bookingModal').style.display = 'none';
}

// Close modal when clicking outside of content
window.onclick = function (event) {
  const modal = document.getElementById('bookingModal');
  if (event.target === modal) {
    modal.style.display = 'none';
  }
};

// Booking form submission with validation and success message
document.addEventListener("DOMContentLoaded", () => {
  const modal = document.getElementById("bookingModal");
  const submitBtn = modal.querySelector("button");
  const inputs = modal.querySelectorAll("input");

  submitBtn.addEventListener("click", () => {
    let valid = true;
    inputs.forEach((input) => {
      if (!input.value.trim()) {
        input.style.border = "2px solid red";
        valid = false;
      } else {
        input.style.border = "";
      }
    });

    if (valid) {
      alert("✅ Booking submitted successfully!");
      inputs.forEach((input) => (input.value = ""));
      closeModal();
    }
  });
});

// Handle contact form submission
function submitEnquiry(event) {
  event.preventDefault();
  alert('📩 Thank you! Your enquiry has been submitted.');
  event.target.reset(); // Clear the form
}

// Scroll back to top
function scrollToTop() {
  window.scrollTo({ top: 0, behavior: 'smooth' });
}

let unifiedRating = 0;

function setUnifiedRating(stars) {
  unifiedRating = stars;
  const starEls = document.querySelectorAll('#unified-stars span');
  starEls.forEach((el, idx) => {
    el.classList.toggle('selected', idx < stars);
  });
}

function submitUnifiedReview(event) {
  event.preventDefault();

  const selected = document.getElementById('reviewTarget').value;
  const reviewText = document.getElementById('unifiedReviewText').value;
  const emoji = document.getElementById('emoji-value').value;


  if (!selected || !reviewText || unifiedRating === 0) {
    alert("Please select a destination, provide rating, and write a review.");
    return;
  }

  const displayDiv = document.getElementById('all-reviews-display');
  const reviewHTML = `
    <div class="review-box">
      <strong>${selected}</strong><br>
      <span>⭐ ${'★'.repeat(unifiedRating)}</span><br>
      <p>${reviewText}</p>
      <p class="emoji-display">${emoji}</p>

    </div>
  `;
  displayDiv.innerHTML += reviewHTML;

  // Reset form
  document.getElementById('reviewTarget').value = '';
  document.getElementById('unifiedReviewText').value = '';
  document.getElementById('emoji-value').value = '';

  setUnifiedRating(0);
}

function submitFeedback(event) {
  event.preventDefault();

  const name = document.getElementById('feedbackName').value;
  const email = document.getElementById('feedbackEmail').value;
  const message = document.getElementById('feedbackMessage').value;

  if (!name || !email || !message) {
    alert("Please fill in all feedback fields.");
    return;
  }

  // Display success (you can replace with API submission or backend call)
  document.getElementById('feedbackSuccess').style.display = 'block';

  // Reset form
  event.target.reset();

  // Optionally hide success after a few seconds
  setTimeout(() => {
    document.getElementById('feedbackSuccess').style.display = 'none';
  }, 4000);
}


  document.addEventListener('DOMContentLoaded', function () {
    const emojis = document.querySelectorAll('.emoji');
    const emojiValue = document.getElementById('emoji-value');

    emojis.forEach(emoji => {
      emoji.addEventListener('click', () => {
        emojis.forEach(e => e.classList.remove('selected')); // clear others
        emoji.classList.add('selected'); // highlight selected
        emojiValue.value = emoji.dataset.value; // store value in hidden input
        console.log("Selected Emoji:", emojiValue.value); // optional: see result

        document.querySelectorAll('.emoji').forEach(emoji => {
    emoji.addEventListener('click', () => {
        document.getElementById('emoji-value').value = emoji.dataset.value;
        console.log("Selected Emoji:", emoji.dataset.value);
    });
});

      });
    });
  });