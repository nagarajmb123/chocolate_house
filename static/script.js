document.addEventListener('DOMContentLoaded', () => {
    //Loading the existing data
    fetchFlavors();
    fetchIngredients();
    fetchSuggestions();
 
    //sunbmit handling
    document.getElementById('flavor-form').addEventListener('submit', addFlavor);
    document.getElementById('ingredient-form').addEventListener('submit', addIngredient);
    document.getElementById('suggestion-form').addEventListener('submit', addSuggestion);
});

//to Fetching and displaying the flavors
function fetchFlavors() {
    fetch('/flavors')
        .then(response => response.json())
        .then(data => {
            const list = document.getElementById('flavors-list');
            list.innerHTML = '';
            data.forEach(flavor => {
                const item = document.createElement('li');
                item.textContent = `${flavor[1]} - ${flavor[2]} `;
                const deleteButton = document.createElement('button');
                deleteButton.textContent = 'Delete';
                deleteButton.onclick = () => deleteFlavor(flavor[0]);
                item.appendChild(deleteButton);
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

function deleteFlavor(flavorId) {
    fetch(`/flavors/${flavorId}`, {
        method: 'DELETE'
    }).then(() => {
        fetchFlavors();
    });
}

//to Fetching and displaying ingredients
function fetchIngredients() {
    fetch('/ingredients')
        .then(response => response.json())
        .then(data => {
            const list = document.getElementById('ingredients-list');
            list.innerHTML = '';
            data.forEach(ingredient => {
                const item = document.createElement('li');
                item.textContent = `${ingredient[1]} - Quantity: ${ingredient[2]} `;
                const deleteButton = document.createElement('button');
                deleteButton.textContent = 'Delete';
                deleteButton.onclick = () => deleteIngredient(ingredient[0]);
                item.appendChild(deleteButton);
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

function deleteIngredient(ingredientId) {
    fetch(`/ingredients/${ingredientId}`, {
        method: 'DELETE'
    }).then(() => {
        fetchIngredients();
    });
}

// Fetching and displaying customer suggestions
function fetchSuggestions() {
    fetch('/suggestions')
        .then(response => response.json())
        .then(data => {
            const list = document.getElementById('suggestions-list');
            list.innerHTML = '';
            data.forEach(suggestion => {
                const item = document.createElement('li');
                item.textContent = `${suggestion[1]} - ${suggestion[2]} (Allergy: ${suggestion[3]}) `;
                const deleteButton = document.createElement('button');
                deleteButton.textContent = 'Delete';
                deleteButton.onclick = () => deleteSuggestion(suggestion[0]);
                item.appendChild(deleteButton);
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

function deleteSuggestion(suggestionId) {
    fetch(`/suggestions/${suggestionId}`, {
        method: 'DELETE'
    }).then(() => {
        fetchSuggestions();
    });
}
