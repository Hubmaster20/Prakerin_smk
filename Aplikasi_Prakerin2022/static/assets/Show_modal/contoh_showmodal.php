<a data-toggle="modal" data-target="#exampleModal" title="Check & Download"><i class="bi bi-briefcase"></i>
                </a>
<div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-body">
        <h4 style="color: #000"><u>DOWNLOAD REFERENSI SKRIPSI</u></h4>
        <table>
        	<tr sty>
        		<td><?php echo $judul_ta;?></td>
        	</tr>
        </table>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
        <button type="button" class="btn btn-primary">Send message</button>
      </div>
    </div>
  </div>
</div>


<script src="<?php echo base_url('assets/Web/assets/js/main.js');?>"></script>

  <script src="<?php echo base_url('assets/Show_modal/jquery-3.2.1.slim.min.js');?>"></script>
  <script src="<?php echo base_url('assets/Show_modal/bootstrap.min.js');?>"></script>
<script type="text/javascript">
$('#exampleModal').on('show.bs.modal', function (event) {
  var button = $(event.relatedTarget) // Button that triggered the modal
  var recipient = button.data('whatever') // Extract info from data-* attributes
  // If necessary, you could initiate an AJAX request here (and then do the updating in a callback).
  // Update the modal's content. We'll use jQuery here, but you could use a data binding library or other methods instead.
  var modal = $(this)
  modal.find('.modal-title').text('New message to ' + recipient)
  modal.find('.modal-body input').val(recipient)
})
</script>
