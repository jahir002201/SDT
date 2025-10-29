const drinkContainer = document.getElementById('drinkContainer');
const searchBtn = document.getElementById('searchBtn');
const searchInput = document.getElementById('searchInput');
const drinkCount = document.getElementById('drinkCount');


let cart = [];

const myFetchDrink = (query = 'a') => {

    return fetch(`https://www.thecocktaildb.com/api/json/v1/1/search.php?s=${query}`)
        .then(res => res.json())
        .then(data => data.drinks);
};

const displayDrinks = (drinks) => {

    drinkContainer.innerHTML = '';


    if (!drinks) {
        drinkContainer.innerHTML = '<h3 class="text-center">Your searched drink is not found</h3>';
        return;
    }


    drinks.forEach(drink => {
        const drinkCard = document.createElement('div');
        drinkCard.classList.add('col');
        drinkCard.innerHTML = `
            <div class="card h-100">
                <img src="${drink.strDrinkThumb}" class="card-img-top" alt="${drink.strGlass}">
                <div class="card-body">
                    <h5 class="card-title"><strong>Name: ${drink.strGlass}</strong></h5>
                    <p class="card-text">Category: ${drink.strCategory}</p>
                    <p class="card-text">Instructions: ${drink.strInstructions.length > 45 ? drink.strInstructions.slice(0, 45) + '...' : drink.strInstructions}</p>
                    <button class="btn btn-info add-to-cart" data-drink='${JSON.stringify({name: drink.strGlass, img: drink.strDrinkThumb})}'>Add to Group</button>
                    <button class="btn btn-warning details-btn" data-id='${drink.idDrink}'>Details</button>
                </div>
            </div>
        `;
        drinkContainer.appendChild(drinkCard);
    });


    const addToCartButtons = () => {
        document.querySelectorAll('.add-to-cart').forEach(button => {
            button.addEventListener('click', (event) => {
                event.target.textContent = 'Already Selected';
            });
        });
    };

    addToCartButtons();

    document.querySelectorAll('.add-to-cart').forEach(button => {
        button.addEventListener('click', addToCart);
    });



    document.querySelectorAll('.details-btn').forEach(button => {
        button.addEventListener('click', showDetails);
    });
};



const addToCart = (event) => {
    if (cart.length >= 7) {
        alert('You cannot add more than 7 drinks to the group.');
        return;
    }
    const drink = JSON.parse(event.target.getAttribute('data-drink'));
    cart.push(drink);
    updateCart();
};



const updateCart = () => {

    drinkCount.textContent = cart.length;

    const tableBody = document.querySelector('table tbody') || document.createElement('tbody');

    tableBody.innerHTML = '';

    cart.forEach((drink, index) => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${index+1}</td>
            <td><img src="${drink.img}" alt="${drink.name}" width="50"></td>
            <td>${drink.name}</td>
        `;
        tableBody.appendChild(row);
    });


    if (!document.querySelector('table tbody')) {
        document.querySelector('table').appendChild(tableBody);
    }
};



const showDetails = (event) => {

    const drinkId = event.target.getAttribute('data-id');

    fetch(`https://www.thecocktaildb.com/api/json/v1/1/lookup.php?i=${drinkId}`)
        .then(res => res.json())
        .then(data => {

            const drink = data.drinks[0];

            const modalContent = `
                <div class="modal fade" id="drinkModal" tabindex="-1" aria-labelledby="drinkModalLabel" aria-hidden="true">
                  <div class="modal-dialog">
                    <div class="modal-content">
                      <div class="modal-header">
                        <h5 class="modal-title" id="drinkModalLabel">${drink.strGlass}</h5>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                      </div>
                      <div class="modal-body">
                        <img src="${drink.strDrinkThumb}" class="img-fluid mb-3" alt="${drink.strDrink}">
                        <p><strong>Details</strong></p>
                        <p>Category:<strong> ${drink.strCategory}</strong></p>
                        <p>Alcoholic:<strong> ${drink.strAlcoholic}</strong></p>
                        <p>${drink.strInstructions}</p>
                      </div>
                      <div class="modal-footer">
                        <button type="button" class="btn btn-danger" data-bs-dismiss="modal">Close</button>
                      </div>
                    </div>
                  </div>
                </div>
            `;

            document.body.insertAdjacentHTML('beforeend', modalContent);
            const drinkModal = new bootstrap.Modal(document.getElementById('drinkModal'));
            drinkModal.show();

            document.getElementById('drinkModal').addEventListener('hidden.bs.modal', () => {
                document.getElementById('drinkModal').remove();
            });

        });
};



searchBtn.addEventListener('click', () => {
    const query = searchInput.value.trim();
    myFetchDrink(query).then(displayDrinks);
});


myFetchDrink().then(displayDrinks);