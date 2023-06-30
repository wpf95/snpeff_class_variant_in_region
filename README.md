# snpeff_class_variant_in_region
Classify the variation types annotated by snpeff into genomic regions

step1: less snpeff.vcf |awk -F"\t|\\\\|" '{printf ("%s\t%s\t%s\t%s\n", $1,$2,$3,$9)}' > input.file  
step2: python anno_region.py input.file > out.file

# vep_class_variant_in_region
run command： python anno_class_vep.py vcf.file > out.file
