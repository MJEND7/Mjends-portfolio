//start of simple weekend code.
function weekend(event) {
  document.getElementById('Display').innerHTML = "well your are free to do anything today :)"
}

//start of the check box code
const checkboxes = document.querySelectorAll('.check-list input[type=checkbox]');
let lastChecked;

function multipleShiftSelector(e) {
  if (e.shiftKey && this.checked) {
    let inBetween = false;

    checkboxes.forEach(checkbox => {
      if (checkbox === this || checkbox === lastChecked) {
        inBetween = !inBetween;
      }

      if (inBetween) {
        checkbox.checked = true;
      }
    });

  }

  lastChecked = this;
}

function checkAll(e) {
  e.preventDefault();
  checkboxes.forEach(checkbox => checkbox.checked = true);
}

function uncheckAll(e) {
  e.preventDefault();
  checkboxes.forEach(checkbox => checkbox.checked = false);
}

checkboxes.forEach(checkbox => checkbox.addEventListener('click', multipleShiftSelector));

document.querySelector('.check-all a').addEventListener('click', checkAll);
document.querySelector('.uncheck-all a').addEventListener('click', uncheckAll);
//end of all code. no duh 