/* ========================
	random meal API script
===========================*/
//Variables
const get_meal_btn = document.getElementById('get_meal');
const meal_container = document.getElementById('meal');

/* Event listener for the click event, the function makes a request to the API */
get_meal_btn.addEventListener('click', () => {
	fetch('https://www.themealdb.com/api/json/v1/1/random.php')
		.then(res => res.json())
		.then(res => {
			createMeal(res.meals[0]);
		})
		.catch(e => {
			console.warn(e);
		});
});


const createMeal = meal => {
	const ingredients = [];

	// Get all ingredients from the object. Up to 20
	for (let i = 1; i <= 20; i++) {
		if (meal[`strIngredient${i}`]) {
			ingredients.push(
				`${meal[`strIngredient${i}`]} - ${meal[`strMeasure${i}`]}`
			);
		} else {
			// Stop if there are no more ingredients
			break;
		}
	}

	const newInnerHTML = `
	<div class="row text-background">
	<div class="col s12">
		<h5 class="form-title recipe-name">
			<p>Your random dish is called:</p>"${meal.strMeal}"
		</h5>
	</div>
	<div class="col s12">
                <img class="recipe-img" src="${meal.strMealThumb}" alt="Meal Image">
            </div>
	<div class="col s12 center">
		<h5 class="form-subtitle">Recipe Tags </h5>
		${meal.strCategory
			? `<p class="chip">${meal.strCategory}</p>`
			: ''
		}
		${meal.strArea ? `<p class="chip">${meal.strArea}</p>` : ''}
		${
		meal.strTags
			? `<p class="chip">${meal.strTags
				.split(',')
				.join(', ')}</p>`
			: ''
		}
	</div>


	<div class="col s12 m6 recipe-padding">
		<h5 class="form-subtitle position">Ingredients</h5>
		<ul>
			${ingredients.map(ingredient => `<li>${ingredient}</li>`).join('')}
		</ul>
	</div>


	<div class="col s12 m6 recipe-padding">
		<h5 class="form-subtitle position">Method</h5>
		<ul class="meal-instr">${meal.strInstructions}</p>
	</div>

<div class="col s12 recipe-padding center-align">
${
		meal.strYoutube
			? `
			
            <iframe width="320" height="215"
			src="https://www.youtube.com/embed/${meal.strYoutube.slice(-11)}" alt="No video available">
		</iframe>
        `
			: ''
		}
		</div>
		</div>`;

	meal_container.innerHTML = newInnerHTML;
};
