$(document).ready(function () {
    // Get references to your rank fields
    var rankFirstField = $('input[name="rank1st"]');
    var rankSecondField = $('input[name="rank2nd"]');
    var rankThirdField = $('input[name="rank3rd"]');
    var rankFourthField = $('input[name="rank4th"]');

    // Define the available choices for each rank
    var choicesForRankSecond = ["cvA", "cvB", "cvC", "cvD"];
    var choicesForRankThird = ["cvA","cvB","cvC", "cvD"];
    var choicesForRankFourth = ["cvA","cvB","cvC", "cvD"];

    // Update choices for rank fields based on the selection in rankFirstField
    rankFirstField.change(function () {
        var selectedValue = $(this).val();

        // Update choices for rankSecondField
        if (selectedValue === "cvA") {
            rankSecondField.find('option[value="cvA"]').remove();
        }

        // Update choices for rankThirdField
        if (selectedValue === "cvC") {
            rankThirdField.find('option[value="cvC"]').remove();
        }

        // Update choices for rankFourthField
        if (selectedValue === "cvD") {
            rankFourthField.find('option[value="cvD"]').remove();
        }
    });
});
