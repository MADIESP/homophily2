<?php
function make_code($llen=4,$nlen=4) {
		$alphabet=explode(",","A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z");
		$a4=array(); for($i=0; $i<$llen; $i++) $a4=array_merge($a4,$alphabet);
		shuffle($a4);
		$code=implode("",array_slice($a4,0,$llen));
		$numbers=str_split("0123456789");
		$n4=array(); for($i=0; $i<$nlen; $i++) $n4=array_merge($n4,$numbers);
		shuffle($n4);
		$code.=implode("",array_slice($n4,0,$nlen));
		return $code;
}

function make_room($rname,$ncodes,$llen=4,$nlen=4,$several_rooms=false,&$globalcodes=null){
	$codes=[];
	while(count($codes)<$ncodes) {
		$ccode=make_code($llen,$nlen);
		if(!in_array($ccode,$codes) && (is_null($globalcodes) || !in_array($ccode,$globalcodes))) {
			$codes[]=$ccode;
			file_put_contents($rname,$ccode."\n", FILE_APPEND);
			if($several_rooms) {
				file_put_contents('all_room_codes.txt',$ccode."\n", FILE_APPEND);
			}
			if (!is_null($globalcodes)) $globalcodes[]=$ccode;
		}
	}
}
$llen=4;$nlen=4;

if($argc>2 && str_replace("room","",$argv[1])==$argv[1]) {
	if($argc>3 && is_numeric($argv[3])) $llen=$argv[3];
	if($argc>4 && is_numeric($argv[4])) $nlen=$argv[4];
	make_room($argv[1],$argv[2],$llen,$nlen);
}

elseif($argc>2) {
	//we make rooms
	$rcodes=[];
	$rllen=5;$rnlen=0;
	$ninside=[40];
	if($argc>3) $ninside=explode(',',$argv[3]);
	if($argc>4 && is_numeric($argv[4])) $llen=$argv[4];
	if($argc>5 && is_numeric($argv[5])) $nlen=$argv[5];
	$nroom=0;
	$all_codes=[];
	while(count($rcodes)<$argv[2]) {
		$ccode=make_code($rllen,$rnlen);
		if(!in_array($ccode,$rcodes)) {
			$rcodes[]=$ccode;
			
			make_room($ccode.".txt",(count($ninside)>$nroom)?$ninside[$nroom]:end($ninside),$llen,$nlen,true,$all_codes);
			$nroom++;
		}
	}
	file_put_contents($argv[1],implode("\n",$rcodes));
	echo "$nroom rooms created :".PHP_EOL; print_r($rcodes);
	echo count(array_unique($all_codes))." unique codes created inside these rooms.";
	///php make_codes.php room_names.txt 10 50,60 3 3
}
?>