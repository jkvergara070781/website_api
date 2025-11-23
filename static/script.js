// Dark mode toggle
const toggleBtn = document.getElementById("darkModeToggle");
const body = document.body;

// Load saved mode
if (localStorage.getItem("theme") === "dark") {
  body.classList.add("dark-mode");
}

// Toggle mode
toggleBtn.addEventListener("click", () => {
  body.classList.toggle("dark-mode");

  const mode = body.classList.contains("dark-mode") ? "dark" : "light";
  localStorage.setItem("theme", mode);
});

// Show loading spinner on navigation
function showSpinner() {
  document.getElementById("loadingSpinner").style.display = "flex";
}
