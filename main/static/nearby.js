// Start from the first image (index 0)
let currentSlide = 0;

// Get all image elements that have the class "slide"
const slides = document.querySelectorAll(".slide");

// Function to show one slide at a time
function showSlides() {
    // Loop through all images and hide them
    slides.forEach((slide, index) => {
        if (index === currentSlide) {
            slide.style.display = "block";  // Show the current slide
        } else {
            slide.style.display = "none";   // Hide all others
        }
    });

    // Move to the next slide (and go back to 0 after the last one)
    currentSlide = (currentSlide + 1) % slides.length;

    // Call this function again after 3 seconds
    setTimeout(showSlides, 3000);
}

// When the web page fully loads, start the slideshow
window.onload = showSlides;
