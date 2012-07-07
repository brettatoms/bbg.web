<?php
/* Plugin Name: Orchid Parameter
Plugin URI: http://belizebotanic.org
Description: Allow orchid and orchid_id parameters to be passed in the URL and recognized by WordPress
Author: Brett
Version: 1.0
Author URI: http://www.belizebotanic.org
*/
add_filter('query_vars', 'parameter_queryvars' );
function parameter_queryvars( $qvars )
{
  $qvars[] = 'orchid';
  $qvars[] = 'orchid_id';
  return $qvars;
}
?>