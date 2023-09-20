
$(document).ready(function () {
    // Get the rank1st select element
    var rank1stSelect = $('#id_rank1st');

    // Set up an event listener for changes in rank1st
    rank1stSelect.change(function () {
        // Get the selected value from rank1st
        var selectedRank1st = rank1stSelect.val();

        // Update the choices for rank2nd based on the selected value for rank1st
        $('#id_rank2nd').empty();
        if (selectedRank1st === 'cvA') {
            $('#id_rank2nd').append($('<option>', {
                value: 'cvB',
                text: 'cvB'
            }));
            $('#id_rank2nd').append($('<option>', {
                value: 'cvC',
                text: 'cvC'
            }));
            $('#id_rank2nd').append($('<option>', {
                value: 'cvD',
                text: 'cvD'
            }));
        } else if (selectedRank1st === 'cvB') {
            $('#id_rank2nd').append($('<option>', {
                value: 'cvA',
                text: 'cvA'
            }));
            // Add other options as needed for cvB
        } else if (selectedRank1st === 'cvC') {
            // Add choices for cvC
        } else if (selectedRank1st === 'cvD') {
            // Add choices for cvD
        }

        // Clear and update the choices for rank3rd and rank4th similarly
        $('#id_rank3rd').empty();
        $('#id_rank4th').empty();
        // Repeat similar logic for rank3rd and rank4th
    });

    // Trigger the change event to initialize rank2nd choices
    rank1stSelect.change();
});
