// Code for Search Overlay
var search_screen = document.getElementById('search-overlay');

$(document).ready(function () {
    $('#search-btn').click(function () {
        $(this).hide();
        $('#search-overlay').fadeIn();
    });
});

window.onclick = function (event) {
    if (event.target == search_screen) {
        search_screen.style.display = 'none';
        $('#search-btn').show();
    }
};

// Materialize Code
$(document).ready(function () {
    $('.button-collapse').sideNav();
    $('select').material_select();
});

$('.button-collapse').sideNav({
    closeOnClick: true, // Closes side-nav on <a> clicks, useful for Angular/Meteor
});

// Code for Adding and Removing Ingredients and Steps on Add Recipe Page
var ingredientField = '<div class="new-ingredient"><div class="input-field"><input placeholder="Next ingredient" type="text" name="recipe_ingredients" class="validate" required></div><div><a class="btn-floating waves-effect waves-light" id="remove_ingredient"> <i class="material-icons icon-color">remove</i></a></div></div>';

var stepField = '<div class="new-method-step"><div class="input-field"><input placeholder="Next step" type="text" name="recipe_method" class="validate" required></div><div><a class="btn-floating waves-effect waves-light" id="remove_method_step"> <i class="material-icons icon-color">remove</i></a></div></div>';

// Add Ingredient to Recipe
$("#add_ingredient").click(function () {
    $("#ingredients").append(ingredientField);
    Materialize.updateTextFields();
});
// Remove the Ingredient from Recipe
$("body").on("click", "#remove_ingredient", function () {
    $(this).parents(".new-ingredient").remove();
});

// Add Step to Recipe Method
$("#add_method_step").click(function () {
    $("#steps").append(stepField);
    Materialize.updateTextFields();
});

// Remove the Ingredient from Recipe
$("body").on("click", "#remove_method_step", function () {
    $(this).parents(".new-method-step").remove();
});

//Code to bind chip input to hidden input field
function updateChipInput(chip) {
    var newval = "";
    newval = $(chip).material_chip('data').reduce(function (result, val) { result.push(val.tag); return result; }, []).join(",");
    $('input[name="recipe_tags"]').val(newval);
}
$(document).ready(function () {
    if ($('.chips')[0]) {
        var data = $('input[name="recipe_tags"]').val().split(',').map(function (tag) {
            return { tag: tag }
        })
        $('.chips').material_chip({
            data: data
        });
        $('.chips-placeholder').material_chip({
            placeholder: 'Tag and hit enter',
            secondaryPlaceholder: 'Next Tag',
        });
        $('.chips').on('chip.add', function (e, chip) {
            updateChipInput(this);
        })
        $('.chips').on('chip.delete', function (e, chip) {
            updateChipInput(this);
        });
    }
});
