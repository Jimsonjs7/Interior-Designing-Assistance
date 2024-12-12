// Wait for DOM to load before running the script
document.addEventListener('DOMContentLoaded', () => {
    // Profile dropdown functionality
    const profileButton = document.getElementById('profileButton');
    const profileDropdown = document.getElementById('profileDropdown');

    // Toggle dropdown visibility on click
    profileButton.addEventListener('click', (event) => {
        event.preventDefault();
        profileDropdown.style.display =
            profileDropdown.style.display === 'block' ? 'none' : 'block';
    });

    // Close dropdown when clicking outside
    document.addEventListener('click', (event) => {
        if (!profileButton.contains(event.target) && !profileDropdown.contains(event.target)) {
            profileDropdown.style.display = 'none';
        }
    });
});
