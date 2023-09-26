$(document).ready(function () {

    // Get the select elements for rankings
    var rank1stSelect = $('#id_rank1st');
    var rank2ndSelect = $('#id_rank2nd').hide();  // Initially hide
    var rank3rdSelect = $('#id_rank3rd').hide();  // Initially hide
    var rank4thSelect = $('#id_rank4th').hide();  // Initially hide

    // Event listeners for changes in rankings
    rank1stSelect.change(function() {
        updateRank2ndChoices();
        rank2ndSelect.show();
    });
    rank2ndSelect.change(function() {
        updateRank3rdChoices();
        rank3rdSelect.show();
    });
    rank3rdSelect.change(function() {
        updateRank4thChoices();
        rank4thSelect.show();


    });

    // Update the available choices for rank2nd based on rank1st selection
    function updateRank2ndChoices() {
        var selectedRank1st = rank1stSelect.val();
        rank2ndSelect.empty();

        var availableChoices = ['cvA', 'cvB', 'cvC', 'cvD'].filter(choice => choice !== selectedRank1st);
        availableChoices.forEach(choice => {
            rank2ndSelect.append($('<option>', { value: choice, text: choice }));
        });
    }

    // Update the available choices for rank3rd based on rank1st and rank2nd selections
    function updateRank3rdChoices() {
        var selectedRank1st = rank1stSelect.val();
        var selectedRank2nd = rank2ndSelect.val();
        rank3rdSelect.empty();

        var availableChoices = ['cvA', 'cvB', 'cvC', 'cvD'].filter(choice => choice !== selectedRank1st && choice !== selectedRank2nd);
        availableChoices.forEach(choice => {
            rank3rdSelect.append($('<option>', { value: choice, text: choice }));
        });

        // Trigger the change event to update rank4th
        rank3rdSelect.change();
    }

    // Update the available choices for rank4th based on rank1st, rank2nd, and rank3rd selections
    function updateRank4thChoices() {
        var selectedRank1st = rank1stSelect.val();
        var selectedRank2nd = rank2ndSelect.val();
        var selectedRank3rd = rank3rdSelect.val();
        rank4thSelect.empty();

        var availableChoices = ['cvA', 'cvB', 'cvC', 'cvD'].filter(choice => choice !== selectedRank1st && choice !== selectedRank2nd && choice !== selectedRank3rd);
        availableChoices.forEach(choice => {
            rank4thSelect.append($('<option>', { value: choice, text: choice }));
        });
    }
});