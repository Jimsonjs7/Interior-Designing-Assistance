document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('measurement-form');
    const recommendationsSection = document.getElementById('recommendations');
    const designSuggestions = document.getElementById('design-suggestions');

    form.addEventListener('submit', function(event) {
        event.preventDefault();
        const spaceSize = document.getElementById('space-size').value;
        
        // Generate recommendations based on the space size
        let recommendations = getRecommendations(spaceSize);

        // Display recommendations
        designSuggestions.innerHTML = recommendations;
        recommendationsSection.classList.remove('hidden');
    });

    function getRecommendations(spaceSize) {
        let recommendations = '';
        
        if (spaceSize <= 500) {
            recommendations = `
                <p>For a small space (${spaceSize} sqft), consider these modern design tips:</p>
                <ul>
                    <li>Use multi-functional furniture to save space.</li>
                    <li>Opt for light colors to make the space feel larger.</li>
                    <li>Incorporate mirrors to enhance light and create an illusion of space.</li>
                </ul>
            `;
        } else if (spaceSize <= 1000) {
            recommendations = `
                <p>For a medium-sized space (${spaceSize} sqft), consider these modern design tips:</p>
                <ul>
                    <li>Create defined zones for different activities.</li>
                    <li>Use a mix of open and closed storage to maintain a clean look.</li>
                    <li>Add statement furniture pieces to anchor the space.</li>
                </ul>
            `;
        } else {
            recommendations = `
                <p>For a large space (${spaceSize} sqft), consider these modern design tips:</p>
                <ul>
                    <li>Use large, bold pieces to fill the space.</li>
                    <li>Incorporate architectural elements like columns or large windows.</li>
                    <li>Experiment with different textures and materials to add depth.</li>
                </ul>
            `;
        }
        
        return recommendations;
    }
});
