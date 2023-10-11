$(document).ready(function () {
    // Get the select elements for rankings
    var rank1stSelect = $('#id_rank1st');
    var rank2ndSelect = $('#id_rank2nd').hide();  // Initially hide
    var rank3rdSelect = $('#id_rank3rd').hide();  // Initially hide
    var rank4thSelect = $('#id_rank4th').hide();  // Initially hide

    // Event listeners for changes in rankings
    rank1stSelect.change(function() {
        updateRankSelect(rank2ndSelect, Constants.INITIAL_CHOICES, rank1stSelect.val());
        rank2ndSelect.show();
    });
    rank2ndSelect.change(function() {
        updateRankSelect(rank3rdSelect, Constants.INITIAL_CHOICES, rank2ndSelect.val());
        rank3rdSelect.show();
    });
    rank3rdSelect.change(function() {
        updateRankSelect(rank4thSelect, Constants.INITIAL_CHOICES, rank3rdSelect.val());
        rank4thSelect.show();
    });

    // Function to update the available choices for a given select element
    function updateRankSelect(selectElement, choices, selectedChoice) {
        selectElement.empty();
        var availableChoices = choices.filter(choice => choice !== selectedChoice);
        availableChoices.forEach(choice => {
            selectElement.append($('<option>', { value: choice, text: choice }));
        });
        selectElement.val(0);
    }
});
