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
    // Function to update choices for rank2nd
// Function to update choices for rank2nd
function updateRank2ndChoices() {
    var selectedRank1st = rank1stSelect.val();
    rank2ndSelect.empty();
    if (selectedRank1st === 'cvA') {
        // Add choices for cvA
        rank2ndSelect.append($('<option>', {
            value: 'cvB',
            text: 'cvB'
        }));
        rank2ndSelect.append($('<option>', {
            value: 'cvC',
            text: 'cvC'
        }));
        rank2ndSelect.append($('<option>', {
            value: 'cvD',
            text: 'cvD'
        }));
    } else if (selectedRank1st === 'cvB') {
        // Add choices for cvB
        rank2ndSelect.append($('<option>', {
            value: 'cvA',
            text: 'cvA'
        }));
        rank2ndSelect.append($('<option>', {
            value: 'cvC',
            text: 'cvC'
        }));
        rank2ndSelect.append($('<option>', {
            value: 'cvD',
            text: 'cvD'
        }));
    } else if (selectedRank1st === 'cvC') {
        // Add choices for cvC
        rank2ndSelect.append($('<option>', {
            value: 'cvA',
            text: 'cvA'
        }));
        rank2ndSelect.append($('<option>', {
            value: 'cvB',
            text: 'cvB'
        }));
        rank2ndSelect.append($('<option>', {
            value: 'cvD',
            text: 'cvD'
        }));
    } else if (selectedRank1st === 'cvD') {
        // Add choices for cvD
        rank2ndSelect.append($('<option>', {
            value: 'cvA',
            text: 'cvA'
        }));
        rank2ndSelect.append($('<option>', {
            value: 'cvB',
            text: 'cvB'
        }));
        rank2ndSelect.append($('<option>', {
            value: 'cvC',
            text: 'cvC'
        }));
    }
}



    // Function to update choices for rank3rd
   // Function to update choices for rank3rd
function updateRank3rdChoices() {
    var selectedRank1st = rank1stSelect.val();
    var selectedRank2nd = rank2ndSelect.val();
    rank3rdSelect.empty();
    if (selectedRank1st === 'cvA') {
        if (selectedRank2nd === 'cvB') {
            // Add choices for cvA and cvC
            rank3rdSelect.append($('<option>', {
                value: 'cvC',
                text: 'cvC'
            }));
            rank3rdSelect.append($('<option>', {
                value: 'cvD',
                text: 'cvD'
            }));
        } else if (selectedRank2nd === 'cvC') {
            // Add choices for cvA and cvB
            rank3rdSelect.append($('<option>', {
                value: 'cvB',
                text: 'cvB'
            }));
            rank3rdSelect.append($('<option>', {
                value: 'cvD',
                text: 'cvD'
            }));
        } else if (selectedRank2nd === 'cvD') {
            // Add choices for cvA and cvB
            rank3rdSelect.append($('<option>', {
                value: 'cvB',
                text: 'cvB'
            }));
            rank3rdSelect.append($('<option>', {
                value: 'cvC',
                text: 'cvC'
            }));
        }
    } else if (selectedRank1st === 'cvB') {
        // Add choices for cvB based on selectedRank2nd
        if (selectedRank2nd === 'cvA') {
            // Add choices for cvB and cvC
            rank3rdSelect.append($('<option>', {
                value: 'cvC',
                text: 'cvC'
            }));
            rank3rdSelect.append($('<option>', {
                value: 'cvD',
                text: 'cvD'
            }));
        } else if (selectedRank2nd === 'cvC') {
            // Add choices for cvB and cvD
            rank3rdSelect.append($('<option>', {
                value: 'cvD',
                text: 'cvD'
            }));
        } else if (selectedRank2nd === 'cvD') {
            // Add choices for cvB and cvC
            rank3rdSelect.append($('<option>', {
                value: 'cvC',
                text: 'cvC'
            }));
        }
    } else if (selectedRank1st === 'cvC') {
        // Add choices for cvC based on selectedRank2nd
        if (selectedRank2nd === 'cvA') {
            // Add choices for cvB and cvC
            rank3rdSelect.append($('<option>', {
                value: 'cvB',
                text: 'cvB'
            }));
            rank3rdSelect.append($('<option>', {
                value: 'cvD',
                text: 'cvD'
            }));
        } else if (selectedRank2nd === 'cvB') {
            // Add choices for cvC and cvD
            rank3rdSelect.append($('<option>', {
                value: 'cvD',
                text: 'cvD'
            }));
        } else if (selectedRank2nd === 'cvD') {
            // Add choices for cvC and cvB
            rank3rdSelect.append($('<option>', {
                value: 'cvB',
                text: 'cvB'
            }));
        }
    } else if (selectedRank1st === 'cvD') {
        // Add choices for cvD based on selectedRank2nd
        if (selectedRank2nd === 'cvA') {
            // Add choices for cvB and cvC
            rank3rdSelect.append($('<option>', {
                value: 'cvB',
                text: 'cvB'
            }));
            rank3rdSelect.append($('<option>', {
                value: 'cvC',
                text: 'cvC'
            }));
        } else if (selectedRank2nd === 'cvB') {
            // Add choices for cvD and cvC
            rank3rdSelect.append($('<option>', {
                value: 'cvC',
                text: 'cvC'
            }));
        } else if (selectedRank2nd === 'cvC') {
            // Add choices for cvD and cvB
            rank3rdSelect.append($('<option>', {
                value: 'cvB',
                text: 'cvB'
            }));
        }
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
        // Add choices for cvA based on selectedRank2nd and selectedRank3rd
        if (selectedRank2nd === 'cvB') {
            // Add choices for cvA and cvD
            rank4thSelect.append($('<option>', {
                value: 'cvD',
                text: 'cvD'
            }));
        } else if (selectedRank2nd === 'cvC') {
            // Add choices for cvA and cvD
            rank4thSelect.append($('<option>', {
                value: 'cvD',
                text: 'cvD'
            }));
        } else if (selectedRank2nd === 'cvD') {
            // Add choices for cvA and cvC
            rank4thSelect.append($('<option>', {
                value: 'cvC',
                text: 'cvC'
            }));
        }
    } else if (selectedRank1st === 'cvB') {
        // Add choices for cvB based on selectedRank2nd and selectedRank3rd
        if (selectedRank2nd === 'cvA') {
            // Add choices for cvB and cvC
            rank4thSelect.append($('<option>', {
                value: 'cvC',
                text: 'cvC'
            }));
        } else if (selectedRank2nd === 'cvC') {
            // Add choices for cvB and cvD
            rank4thSelect.append($('<option>', {
                value: 'cvD',
                text: 'cvD'
            }));
        } else if (selectedRank2nd === 'cvD') {
            // Add choices for cvB and cvC
            rank4thSelect.append($('<option>', {
                value: 'cvC',
                text: 'cvC'
            }));
        }
    } else if (selectedRank1st === 'cvC') {
        // Add choices for cvC based on selectedRank2nd and selectedRank3rd
        if (selectedRank2nd === 'cvA') {
            // Add choices for cvC and cvD
            rank4thSelect.append($('<option>', {
                value: 'cvD',
                text: 'cvD'
            }));
        } else if (selectedRank2nd === 'cvB') {
            // Add choices for cvC and cvD
            rank4thSelect.append($('<option>', {
                value: 'cvD',
                text: 'cvD'
            }));
        } else if (selectedRank2nd === 'cvD') {
            // Add choices for cvC and cvB
            rank4thSelect.append($('<option>', {
                value: 'cvB',
                text: 'cvB'
            }));
        }
    } else if (selectedRank1st === 'cvD') {
        // Add choices for cvD based on selectedRank2nd and selectedRank3rd
        if (selectedRank2nd === 'cvA') {
            // Add choices for cvD and cvC
            rank4thSelect.append($('<option>', {
                value: 'cvC',
                text: 'cvC'
            }));
        } else if (selectedRank2nd === 'cvB') {
            // Add choices for cvD and cvC
            rank4thSelect.append($('<option>', {
                value: 'cvC',
                text: 'cvC'
            }));
        } else if (selectedRank2nd === 'cvC') {
            // Add choices for cvD and cvB
            rank4thSelect.append($('<option>', {
                value: 'cvB',
                text: 'cvB'
            }));
        }
    }
}

});
