# snpeff_class_variant_in_region
Classify the variation types annotated by snpeff into genomic regions

step1: less snpeff.vcf |awk -F"\t|\\\\|" '{printf ("%s\t%s\t%s\t%s\n", $1,$2,$3,$9)}' > input.file  
step2: python anno_region.py input.file > out.file
