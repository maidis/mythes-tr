BEGIN { FS = "\t" }
{   a[$1] = a[$1] "|" $2 }
END { for (item in a ) print item, a[item] }
