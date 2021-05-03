/* retrieve cupcake info from DB */

BASE_API_URL = "http://localhost:5000/api/cupcakes"

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

async function addCupcake({ flavor, size, rating, image }) {
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
}

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

async function addNewCupcake(evt) {
  evt.preventDefault();
  console.log("addnewuppie)")
  let $flavor = $('#flavor').val();
  let $size = $('#size').val();
  let $rating = $('#rating').val();
  let $image = $('#image').val();
  let newCupcake = await addCupcake({ $flavor, $size, $rating, $image });
}

$('#cupcake-form').on("submit", addNewCupcake);

getCupcakeInfo();