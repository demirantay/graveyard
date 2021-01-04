/*
  Module: Auto Correcting Text (auto_correct.js)

  Desc: In this module the scirpt gets the value of the text input and
        checks it weatcher it is spelled correctly or wrong. If it is
        wrong it outputs a `did you mean: **` value where the stars will
        be the calculated guess of the meant value.
*/


// get the DOM objcts of text input
form = document.getElementById("autocorrecting-text-form");
text_input = document.getElementById("autocorrecting-text-input");

// get the dom objs of did you mean output
autocorrect_guess = document.getElementById("autocorrect-program-guess");

// sorted en word list where it will check weather it is in the list
english_word_list = ["the","of","and","a","to","in","is","you","that","it","he",
"was","for","on","are","as","with","his","they","I","at","be","this","have",
"from","or","one","had","by","word","but","not","what","all","were","we",
"when","your","can","said","there","use","an","each","which","she","do","how",
"their","if","will","up","other","about","out","many","then","them","these","so"
,"some","her","would","make","like","him","into","time","has","look","two",
"more","write","go","see","number","no","way","could","people","my","than",
"first","water","been","call","who","oil","its","now","find","long","down",
"day","did","get","come","made","may","part"]

// Reverse hamming distance algorithm (cheks similiarities rather than differences)
function reverse_hamming_distance(string1, string2) {
  let hamming_distance = 0;
  if (string1.length !== string2.length) {
    return 0;
  }
  else {
    for (let i = 0; i < string1.length; i++) {
      if (string1[i] === string2[i]) {
        hamming_distance++;
      } else {
        continue;
      }
    }
    return hamming_distance;
  }
}

function get_most_similar_word() {
  hamming_points = 0;
  hamming_points_index = 0;

  for (let i = 0; i < english_word_list.length; i++) {
    current_hamming_iteration = reverse_hamming_distance(text_input.value, english_word_list[i]);
    if (hamming_points < current_hamming_iteration) {
      hamming_points = current_hamming_iteration;
      hamming_points_index = i;
    }
    else {
      continue;
    }
  }

  if (text_input.value.length > 0) {
    autocorrect_guess.innerHTML = english_word_list[hamming_points_index];
  }
  else {
    autocorrect_guess.innerHTML = "";
  }
}
