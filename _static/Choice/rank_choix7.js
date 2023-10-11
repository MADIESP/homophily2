$(document).ready(function () {
    // Get the select elements for rankings
    var rank1stSelect = $('#id_rank1st');
    var rank2ndSelect = $('#id_rank2nd').hide();  // Initially hide
    var rank3rdSelect = $('#id_rank3rd').hide();  // Initially hide
    var rank4thSelect = $('#id_rank4th').hide();  // Initially hide

    // Event listeners for changes in rankings
    rank1stSelect.change(function() {
        C.CHOICES = updateChoices(C.CHOICES, rank1stSelect.val());
        updateRankSelect(rank2ndSelect, C.CHOICES);
        rank2ndSelect.show();
    });
    rank2ndSelect.change(function() {
        C.CHOICES = updateChoices(C.CHOICES, rank2ndSelect.val());
        updateRankSelect(rank3rdSelect, C.CHOICES);
        rank3rdSelect.show();
    });
    rank3rdSelect.change(function() {
        C.CHOICES = updateChoices(C.CHOICES, rank3rdSelect.val());
        updateRankSelect(rank4thSelect, C.CHOICES);
        rank4thSelect.show();
    });

    // Function to update the available choices for a given select element
    function updateRankSelect(selectElement, choices) {
        selectElement.empty();
        choices.forEach(choice => {
            selectElement.append($('<option>', { value: choice, text: choice }));
        });
        selectElement.val(0);
    }

    // Function to update the choices based on the selected choice
    function updateChoices(choices, selectedChoice) {
        return choices.filter(choice => choice !== selectedChoice);
    }
});
