import sys, tempfile, os
from subprocess import call

EDITOR = os.environ.get('EDITOR','vim') #that easy!

if EDITOR in ['vim', 'nvim']:
    EXTRA_EDITOR_COMMAND = '+set backupcopy=yes'
else:
    EXTRA_EDITOR_COMMAND = None

initial_message = "hello world" # if you want to set up the file somehow

with tempfile.NamedTemporaryFile(suffix=".tmp") as tf:
  tf.write(initial_message)
  tf.flush()
  if extra_editor_command:
      call([EDITOR, extra_editor_command, tf.name])
  else:
      call([EDITOR, tf.name])



  # do the parsing with `tf` using regular File operations.
  # for instance:
  tf.seek(0)
  edited_message = tf.read()
  print edited_message
