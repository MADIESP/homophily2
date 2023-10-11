$(document).ready(function () {
    // Get the select elements for rankings
    var rank1stSelect = $('#id_rank1st');
    var rank2ndSelect = $('#id_rank2nd').hide();  // Initially hide
    var rank3rdSelect = $('#id_rank3rd').hide();  // Initially hide
    var rank4thSelect = $('#id_rank4th').hide();  // Initially hide

    // Event listeners for changes in rankings
    rank1stSelect.change(function() {
        updateRank2ndChoices(rank1stSelect.val());
        rank2ndSelect.show();
        rank3rdSelect.hide();
        rank4thSelect.hide();
    });
    rank2ndSelect.change(function() {
        updateRank3rdChoices(rank1stSelect.val(), rank2ndSelect.val());
        rank3rdSelect.show();
        rank4thSelect.hide();
    });
    rank3rdSelect.change(function() {
        updateRank4thChoices(rank1stSelect.val(), rank2ndSelect.val(), rank3rdSelect.val());
        rank4thSelect.show();
    });

    // Function to update the available choices for rank2nd based on rank1st selection
    function updateRank2ndChoices(selectedRank1st) {
        var availableChoices = ['cvA', 'cvB', 'cvC', 'cvD'].filter(choice => choice !== selectedRank1st);
        rank2ndSelect.empty();
        availableChoices.forEach(choice => {
            rank2ndSelect.append($('<option>', { value: choice, text: choice }));
        });
        rank2ndSelect.val(0);
    }

    // Function to update the available choices for rank3rd based on rank1st and rank2nd selections
    function updateRank3rdChoices(selectedRank1st, selectedRank2nd) {
        var availableChoices = ['cvA', 'cvB', 'cvC', 'cvD'].filter(choice => choice !== selectedRank1st && choice !== selectedRank2nd);
        rank3rdSelect.empty();
        availableChoices.forEach(choice => {
            rank3rdSelect.append($('<option>', { value: choice, text: choice }));
        });
        rank3rdSelect.val(0);
    }

    // Function to update the available choices for rank4th based on rank1st, rank2nd, and rank3rd selections
    function updateRank4thChoices(selectedRank1st, selectedRank2nd, selectedRank3rd) {
        var availableChoices = ['cvA', 'cvB', 'cvC', 'cvD'].filter(choice => choice !== selectedRank1st && choice !== selectedRank2nd && choice !== selectedRank3rd);
        rank4thSelect.empty();
        availableChoices.forEach(choice => {
            rank4thSelect.append($('<option>', { value: choice, text: choice }));
        });
        rank4thSelect.val(0);
    }
});
