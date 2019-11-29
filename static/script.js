/* random meal API script */
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
			<h4 class="random-meal-name"><p>Your random dish is called:</p>"${meal.strMeal}"</h4>
			
			<div class="img-header-parent">
				<h4 class="image-header">${meal.strMeal}</h4>
			</div>

			<div class="tags">
				${meal.strCategory
			? `<p class="meal-info"><strong>Category:</strong> ${meal.strCategory}</p>`
			: ''
		}
						${meal.strArea ? `<p class="meal-info"><strong>Area:</strong> ${meal.strArea}</p>` : ''}
						${
		meal.strTags
			? `<p class="meal-info"><strong>Tags:</strong> ${meal.strTags
				.split(',')
				.join(', ')}</p>`
			: ''
		}
			</div>

			<div class="tags-parent">
			<h6 class="tags-header">tags:</h6>
			</div>
			<div class="img-food-parent">
				<img class="img-food" src="${meal.strMealThumb}" alt="Meal Image">
			</div>
			<div class="ingr-parent">
				<h6 class="ingr-header">Ingredients:</h6>
			</div>
				<div class="ingredients">
					<ul>
						${ingredients.map(ingredient => `<li>${ingredient}</li>`).join('')}
					</ul>
			</div>
		
			<div class="meal-instr-parent">
				<h6 class="meal-instr-header">Prepartions:</h6>
			</div>
				<div class="instructions">
				<p class="meal-instr">${meal.strInstructions}</p>
			</div>
		</div>
		${
		meal.strYoutube
			? `
		<div class="video-parent">
		<div class="videoWrapper">
			<iframe width="320" height="215"
				src="https://www.youtube.com/embed/${meal.strYoutube.slice(-11)}" alt="No video available">
			</iframe>
		</div>
		</div>`
			: ''
		}
	`;

	meal_container.innerHTML = newInnerHTML;
};
