// i18n logic for client-side text changes (if any) and language toggle

document.addEventListener("DOMContentLoaded", () => {
  const langToggle = document.getElementById("langToggle");
  const currentLang = localStorage.getItem("lang") || "en";

  // Initialize lang
  if (currentLang === "hi") {
    document.documentElement.lang = "hi";
  }

  if (langToggle) {
    langToggle.addEventListener("click", () => {
      const newLang = document.documentElement.lang === "hi" ? "en" : "hi";
      document.documentElement.lang = newLang;
      localStorage.setItem("lang", newLang);
      window.location.reload(); // Reload to fetch server-rendered translated content
    });
  }
});
