# time：2023/5/10 17:04
# name：Wangpf
# encoding：utf-8

#usage:python .py [snpeff.txt] > [out.file]

import sys
fo=open(sys.argv[1],'r')

# priority: CDS > 5’UTR > 3’UTR > intron > intergenic regions
rule = ['CDS','5_prime_UTR_variant','3_prime_UTR_variant','intron_variant','intergenic_region']

# classification of region by variation types
CDS=['conservative_inframe_deletion','conservative_inframe_insertion','disruptive_inframe_deletion','disruptive_inframe_insertion','frameshift_variant','intragenic_variant','missense_variant','synonymous_variant','start_lost','stop_gained','stop_lost']
intron_variant=['intron_variant','non_coding_transcript_exon_variant','splice_acceptor_variant','splice_region_variant','splice_donor_variant']
intergenic_region=['intergenic_region','downstream_gene_variant','upstream_gene_variant']

for line in fo:
    line = line.strip().split()
    types = line[3].split(',')
    head = '\t'.join(line[:3])
    if len(types) == 1:
        type = ''.join(types)
        if type in CDS:
            print(head+"\t"+'CDS')
        elif type in intergenic_region:
            print(head+"\t"+'intergenic_region')
        elif type in intron_variant:
            print(head+"\t"+'intron_variant')
        elif type =='3_prime_UTR_variant':
            print(head+"\t"+'3_prime_UTR_variant')
        elif type =='5_prime_UTR_variant':
            print(head+"\t"+'5_prime_UTR_variant')
        else:
            pass
    else:
        temp = []
        for type in types:
            if type in CDS:
                temp.append(rule.index('CDS'))
            elif type in intergenic_region:
                temp.append(rule.index('intergenic_region'))
            elif type =='5_prime_UTR_variant':
                temp.append(rule.index('5_prime_UTR_variant'))
            elif type =='3_prime_UTR_variant':
                temp.append(rule.index('3_prime_UTR_variant'))
            elif type in intron_variant:
                temp.append(rule.index('intron_variant'))
            else:
                pass
        print(head+"\t"+rule[min(temp)])


