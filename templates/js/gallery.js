var numImgInFolder = 10 //should be connected with database to find out the number for each gallery catagory (backend should be attached here)

// dynamically create loads of image cells
/**function cells(count) {
  if (typeof count !== 'number' || count > 99) return false;

  var html = '',
    imageNum;
  var folderName = '600/'

  for (i = 0; i < count; i++) {
    //imageNum = Math.floor(Math.random() * 9) + 1;
    html += '<article class="image__cell is-collapsed">' +
      '<div class="image--basic">' +
      '<a href="#expand-jump-' + i + '">' +
      '<div style="height:200px; display: inline-flex">' +
      '<img id="expand-jump-' + i + '" class="basic__img" src="img/galleryimg/' + folderName + i + '.jpg" alt="Fashion ' + i + '" />' +
      '</div>' +
      '</a>' +
      '<div class="arrow--up"></div>' +
      '</div>' +
      '<div class="image--expand">' +
      '<a href="#close-jump-' + i + '" class="expand__close"></a>' +
      '<img class="image--large" src="img/galleryimg/' + folderName + i + '.jpg" alt="Fashion ' + i + '" />' +
      '</div>' +
      '</article>';
  }
  return html;
}

//apend cells to grid
$('.image-grid').empty().html(cells(numImgInFolder));
**/

//bind click events
var $cell = $('.image__cell');

$cell.find('.image--basic').click(function() {
  var $thisCell = $(this).closest('.image__cell');

  if ($thisCell.hasClass('is-collapsed')) {
    $cell.not($thisCell).removeClass('is-expanded').addClass('is-collapsed');
    $thisCell.removeClass('is-collapsed').addClass('is-expanded');
  } else {
    $thisCell.removeClass('is-expanded').addClass('is-collapsed');
  }
});

$cell.find('.expand__close').click(function() {

  var $thisCell = $(this).closest('.image__cell');

  $thisCell.removeClass('is-expanded').addClass('is-collapsed');
});
