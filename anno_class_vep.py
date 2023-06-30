import sys
fo = open(sys.argv[1], 'r')

# priority: CDS > 5’UTR > 3’UTR > upstream_gene_variant > intron > intergenic regions
rule = ['CDS', '5_prime_UTR_variant', '3_prime_UTR_variant', 'upstream_gene_variant','intron_variant', 'intergenic_region']

# classification of region by variation types
CDS = ['coding_sequence_variant', 'frameshift_variant', 'inframe_deletion', 'inframe_insertion', 'missense_variant', 'protein_altering_variant', 'start_lost', 'start_retained_variant', 'stop_gained', 'stop_lost', 'stop_retained_variant', 'synonymous_variant']
intron_variant = ['intron_variant', 'non_coding_transcript_exon_variant', 'non_coding_transcript_variant', 'splice_acceptor_variant', 'splice_donor_5th_base_variant', 'splice_donor_region_variant', 'splice_donor_variant', 'splice_polypyrimidine_tract_variant', 'splice_region_variant']
intergenic_region = ['intergenic_variant', 'downstream_gene_variant']

for line in fo:
    if line.startswith('#'):
        pass
    else:
        line = line.strip().split()
        head = line[0]
        types= line[6].split(',')
        pos = line[1]
        chrom = line[1].split(':')[0]
        start = line[1].split(':')[1].split('-')[0]
        end = line[1].split(':')[1].split('-')[1]
        if len(types) == 1:
            type = ''.join(types)
            if type in CDS:
                print(chrom + "\t" + start + "\t" + end + "\t" + head + "\t" + 'CDS')
            elif type in intergenic_region:
                print(chrom + "\t" + start + "\t" + end + "\t" + head + "\t" + 'intergenic_region')
            elif type in intron_variant:
                print(chrom + "\t" + start + "\t" + end + "\t" + head + "\t" + 'intron_variant')
            elif type == '3_prime_UTR_variant':
                print(chrom + "\t" + start + "\t" + end + "\t" + head + "\t" + '3_prime_UTR_variant')
            elif type == '5_prime_UTR_variant':
                print(chrom + "\t" + start + "\t" + end + "\t" + head + "\t" + '5_prime_UTR_variant')
            elif type == 'upstream_gene_variant':
                print(chrom + "\t" + start + "\t" + end + "\t" + head + "\t" + 'upstream_gene_variant')
            else:
                pass
        else:
            temp = []
            for type in types:
                if type in CDS:
                    temp.append(rule.index('CDS'))
                elif type in intergenic_region:
                    temp.append(rule.index('intergenic_region'))
                elif type == '5_prime_UTR_variant':
                    temp.append(rule.index('5_prime_UTR_variant'))
                elif type == '3_prime_UTR_variant':
                    temp.append(rule.index('3_prime_UTR_variant'))
                elif type == 'upstream_gene_variant':
                    temp.append(rule.index('upstream_gene_variant'))
                elif type in intron_variant:
                    temp.append(rule.index('intron_variant'))
                else:
                    pass
            print(chrom + "\t" + start + "\t" + end + "\t" + head + "\t" + rule[min(temp)])


