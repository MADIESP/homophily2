// Assuming you have HTML elements with IDs for rank fields like 'id_rank1st', 'id_rank2nd', 'id_rank3rd', 'id_rank4th'
const rank1stField = document.getElementById('id_rank1st');
const rank2ndField = document.getElementById('id_rank2nd');
const rank3rdField = document.getElementById('id_rank3rd');
const rank4thField = document.getElementById('id_rank4th');

// Define the available choices for rank2nd, rank3rd, and rank4th
const allChoices = ['cvA', 'cvB', 'cvC', 'cvD'];

rank1stField.addEventListener('change', function () {
    // Get the selected value of rank1st
    const selectedRank1st = rank1stField.value;

    // Create an array of choices excluding the selected value in rank1st
    const availableChoices = allChoices.filter(choice => choice !== selectedRank1st);

    // Update the options for rank2nd, rank3rd, and rank4th
    updateSelectOptions(rank2ndField, availableChoices);
    updateSelectOptions(rank3rdField, availableChoices);
    updateSelectOptions(rank4thField, availableChoices);
});

function updateSelectOptions(selectField, choices) {
    // Clear existing options
    selectField.innerHTML = '';

    // Add new options based on the available choices
    for (const choice of choices) {
        const option = document.createElement('option');
        option.value = choice;
        option.text = choice;
        selectField.appendChild(option);
    }
}

// Initialize the available choices when the page loads
updateSelectOptions(rank2ndField, allChoices);
updateSelectOptions(rank3rdField, allChoices);
updateSelectOptions(rank4thField, allChoices);
