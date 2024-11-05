

document.addEventListener('DOMContentLoaded', () => {
    // Load the  existing data
    fetchFlavors();
    fetchIngredients();
    fetchSuggestions();

    // Handling the submissions
    document.getElementById('flavor-form').addEventListener('submit', addFlavor);
    document.getElementById('ingredient-form').addEventListener('submit', addIngredient);
    document.getElementById('suggestion-form').addEventListener('submit', addSuggestion);
});

// Fetching and displaying the flavors
function fetchFlavors() {
    fetch('/flavors')
        .then(response => response.json())
        .then(data => {
            const list = document.getElementById('flavors-list');
            list.innerHTML = '';
            data.forEach(flavor => {
                const item = document.createElement('li');
                item.textContent = `${flavor[1]} - ${flavor[2]}`;
                list.appendChild(item);
            });
        });
}

function addFlavor(event) {
    event.preventDefault();
    const name = document.getElementById('flavor-name').value;
    const description = document.getElementById('flavor-description').value;

    fetch('/flavors', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ flavor_name: name, description: description })
    }).then(() => {
        document.getElementById('flavor-form').reset();
        fetchFlavors();
    });
}

//Fetching and displaying ingredients
function fetchIngredients() {
    fetch('/ingredients')
        .then(response => response.json())
        .then(data => {
            const list = document.getElementById('ingredients-list');
            list.innerHTML = '';
            data.forEach(ingredient => {
                const item = document.createElement('li');
                item.textContent = `${ingredient[1]} - Quantity: ${ingredient[2]}`;
                list.appendChild(item);
            });
        });
}

function addIngredient(event) {
    event.preventDefault();
    const name = document.getElementById('ingredient-name').value;
    const quantity = document.getElementById('ingredient-quantity').value;

    fetch('/ingredients', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ ingredient_name: name, quantity: quantity })
    }).then(() => {
        document.getElementById('ingredient-form').reset();
        fetchIngredients();
    });
}

//Fetching and displaying customersuggestions
function fetchSuggestions() {
    fetch('/suggestions')
        .then(response => response.json())
        .then(data => {
            const list = document.getElementById('suggestions-list');
            list.innerHTML = '';
            data.forEach(suggestion => {
                const item = document.createElement('li');
                item.textContent = `${suggestion[1]} - ${suggestion[2]} (Allergy: ${suggestion[3]})`;
                list.appendChild(item);
            });
        });
}

function addSuggestion(event) {
    event.preventDefault();
    const customerName = document.getElementById('customer-name').value;
    const suggestionText = document.getElementById('suggestion-text').value;
    const allergyConcern = document.getElementById('allergy-concern').value;

    fetch('/suggestions', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            customer_name: customerName,
            suggestion: suggestionText,
            allergy_concern: allergyConcern
        })
    }).then(() => {
        document.getElementById('suggestion-form').reset();
        fetchSuggestions();
    });
}
