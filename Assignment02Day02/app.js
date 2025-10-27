document.getElementById('searchButton').addEventListener('click', () => {
    const query = document.getElementById('searchInput').value;
    fetchMeals(query);
});

const fetchMeals = (query) => {
    fetch(`https://www.themealdb.com/api/json/v1/1/search.php?s=${query}`)
        .then(response => response.json())
        .then(data => displayMeals(data.meals))
        .catch(error => console.error('Error fetching data:', error));
};

const displayMeals = (meals) => {
  const container = document.querySelector('.container');
  container.innerHTML = `
      <div class="row mb-3 center-align">
          <div class="col-md-8">
              <input type="text" id="searchInput" class="form-control" placeholder="Find your favorite food">
          </div>
          <div class="col-md-4">
              <button id="searchButton" class="btn btn-warning">Search</button>
          </div>
      </div>
      <div class="row" id="mealsRow"></div>
  `;

  document.getElementById('searchButton').addEventListener('click', () => {
      const query = document.getElementById('searchInput').value;
      fetchMeals(query);
  });

  const mealsRow = document.getElementById('mealsRow');

  if (!meals) {
      mealsRow.innerHTML = '<p>No meals found.</p>';
      return;
  }

  for (const meal of meals) {
      const { strMeal, strMealThumb } = meal;

      const mealCard = document.createElement('div');
      mealCard.classList.add('col-md-4', 'mb-4');
      mealCard.innerHTML = `
          <div id="clickCard" class="card h-100 shadow bg-body rounded text-center">
              <img src="${strMealThumb}" class="card-img-top" alt="${strMeal}">
              <div class="card-body">
              <input type="hidden" class="meal-id" value="${meal.idMeal}">
                  <h5 class="card-title text-info fs-1">${strMeal}</h5>
              </div>
          </div>
      `;
      mealsRow.appendChild(mealCard);
  }
};

document.addEventListener('click', (event) => {
    if (event.target.closest('#clickCard')) {
        const mealCard = event.target.closest('#clickCard');
        const mealId = mealCard.querySelector('.meal-id').value;
        fetchMealDetails(mealId);
    }
});

const fetchMealDetails = (mealId) => {
    fetch(`https://www.themealdb.com/api/json/v1/1/lookup.php?i=${mealId}`)
        .then(response => response.json())
        .then(data => displayMealDetails(data.meals[0]))
        .catch(error => console.error('Error fetching meal details:', error));
};

const displayMealDetails = (meal) => {
    const container = document.querySelector('.container');
    let detailCard = document.getElementById('detailCard');

    if (!detailCard) {
        detailCard = document.createElement('div');
        detailCard.id = 'detailCard';
        container.prepend(detailCard);
    }

    const { strMeal, strMealThumb } = meal;

    detailCard.innerHTML = `
        <div class="row mb-4">
        <div class="col-md-6 offset-md-3">
        <div class="card h-100 shadow bg-body rounded">     
              <img src="${strMealThumb}" class="card-img-top" alt="${strMeal}">
              <div class="card-body">
                  <h5 class="card-title text-info fs-1">${strMeal}</h5>
                  <p class="fs-3">Ingredients</p>
                  <ul>
                    <li>${meal.strIngredient1}</li>
                    <li>${meal.strIngredient2}</li>
                    <li>${meal.strIngredient3}</li>
                    <li>${meal.strIngredient4}</li>
                    <li>${meal.strIngredient5}</li>
                    <li>${meal.strIngredient6}</li>
                    <li>${meal.strIngredient7}</li>
                    <li>${meal.strIngredient8}</li>
                    <li>${meal.strIngredient9}</li>
                  </ul>
              </div>
        </div>
        </div>
    `;
};