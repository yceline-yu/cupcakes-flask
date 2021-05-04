/* retrieve cupcake info from DB */

BASE_API_URL = "http://localhost:5000/api/cupcakes"
/* turn cupcake object into html list item */
function generateCupcakeMarkup(cupcake) {
  console.log("markup running!")
  console.log("cupcake.id ==>", cupcake.id)
  return $(`   
    <li id="${cupcake.id}">
          <a href="/api/cupcakes/${cupcake.id}" class="cupcake-link">
            ${cupcake.flavor}
          </a>
        </li>
      `);
}

/* send new cupcake to back end (which adds to DB) and add to cupcake list */
async function addCupcake({ flavor, size, rating, image }) {
  console.log("ADD CC() flavor ==>",flavor)
  const response = await axios({
    url: `${BASE_API_URL}`,
    method: "POST",
    data: {
      flavor,
      size,
      rating,
      image
    }
  });
  // could split this into two functions?
  console.log("addCupcake() REST ==>", response)
  let newCupcake = generateCupcakeMarkup(response.data.cupcake)
  $('#cupcake-list').append(newCupcake)

}

/* get all cupcakes from DB and append to cupcake list */
async function getCupcakeInfo() {
  // evt.preventDefault();
  let response = await axios.get(BASE_API_URL);
  // console.log("this is the resp", response);
  let cupcakes = response.data.cupcakes;
  // console.log("This is cupcakes from resp", cupcakes);
  for (let cupcake of cupcakes) {
    // console.log("looping?!")
    // console.log("cupcake =>", cupcake);
    let cupcakeMarkup = generateCupcakeMarkup(cupcake);
    $('#cupcake-list').append(cupcakeMarkup);
  }
}
/* retrieves form data and sends form info to back end  */
async function addNewCupcake(evt) {
  evt.preventDefault();
  console.log("addnewuppie)")
  let $flavor = $("#flavor").val()
  let $size = $("#size").val();
  let $rating = $('#rating').val();
  let $image = $('#image').val();
  await addCupcake({ "flavor":$flavor,
                                       "size":$size, 
                                       "rating":$rating, 
                                       "image":$image 
                                      });
}

// event listener on new cupcake submit button 
$('#cupcake-form').on("submit", addNewCupcake);
// populates page with cupcake list
getCupcakeInfo();