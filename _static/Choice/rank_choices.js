$(document).ready(function () {
    // Get the select elements for rank1st, rank2nd, rank3rd, and rank4th
    var rank1stSelect = $('#id_rank1st');
    var rank2ndSelect = $('#id_rank2nd');
    var rank3rdSelect = $('#id_rank3rd');
    var rank4thSelect = $('#id_rank4th');

    // Set up event listeners for changes in rank1st, rank2nd, and rank3rd
    rank1stSelect.change(function () {
        updateRank2ndChoices();
    });

    rank2ndSelect.change(function () {
        updateRank3rdChoices();
    });

    rank3rdSelect.change(function () {
        updateRank4thChoices();
    });

    // Function to update choices for rank2nd
    function updateRank2ndChoices() {
        var selectedRank1st = rank1stSelect.val();
        rank2ndSelect.empty();
        if (selectedRank1st === 'cvA') {
            // Add choices for cvA
        } else if (selectedRank1st === 'cvB') {
            // Add choices for cvB
        } else if (selectedRank1st === 'cvC') {
            // Add choices for cvC
        } else if (selectedRank1st === 'cvD') {
            // Add choices for cvD
        }
        // Trigger the change event to update rank3rd and rank4th
        rank2ndSelect.change();
    }

    // Function to update choices for rank3rd
    function updateRank3rdChoices() {
        var selectedRank1st = rank1stSelect.val();
        var selectedRank2nd = rank2ndSelect.val();
        rank3rdSelect.empty();
        if (selectedRank1st === 'cvA') {
            // Add choices for cvA
        } else if (selectedRank1st === 'cvB') {
            // Add choices for cvB
        } else if (selectedRank1st === 'cvC') {
            // Add choices for cvC
        } else if (selectedRank1st === 'cvD') {
            // Add choices for cvD
        }
        // Trigger the change event to update rank4th
        rank3rdSelect.change();
    }

    // Function to update choices for rank4th
    function updateRank4thChoices() {
        var selectedRank1st = rank1stSelect.val();
        var selectedRank2nd = rank2ndSelect.val();
        var selectedRank3rd = rank3rdSelect.val();
        rank4thSelect.empty();
        if (selectedRank1st === 'cvA') {
            // Add choices for cvA
        } else if (selectedRank1st === 'cvB') {
            // Add choices for cvB
        } else if (selectedRank1st === 'cvC') {
            // Add choices for cvC
        } else if (selectedRank1st === 'cvD') {
            // Add choices for cvD
        }
    }

    // Initialize choices for rank2nd
    updateRank2ndChoices();
});
