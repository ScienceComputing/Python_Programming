# Ref: https://slides.com/johanneskoester/deck-1

SAMPLES = glob_wildcards("data/samples/{fname}.fastq").fname
print(SAMPLES)

configfile: "config.yaml"

# SAMPLES = ["A", "B"]

rule all:
    input:
        "plots/quals.svg"

def get_bwa_map_input_fastqs(wildcards):
    return config["samples"][wildcards.sample]

include: "read_map.snakefile"


# rule bwa_map:
#     input:
#         "data/genome.fa",
#         get_bwa_map_input_fastqs
#     output:
#         temp("mapped_reads/{sample}.bam") # Modify here
#     params:
#         rg=r"@RG\tID:{sample}\tSM:{sample}"
#     log:
#         "logs/bwa_mem/{sample}.log"
#     benchmark:
#         repeat("benchmarks/{sample}.bwa.benchmark.txt", 3)
#     threads: 8
#     shell:
#         "(bwa mem -R '{params.rg}' -t {threads} {input} | "
#         "samtools view -Sb - > {output}) 2> {log}"

# rule bwa_map:
#     input:
#         "data/genome.fa",
#         get_bwa_map_input_fastqs
#     output:
#         "mapped_reads/{sample}.bam"
#     params:
#         rg=r"@RG\tID:{sample}\tSM:{sample}"
#     log:
#         "logs/bwa_mem/{sample}.log"
#     threads: 8
#     shell:
#         "(bwa mem -R '{params.rg}' -t {threads} {input} | "
#         "samtools view -Sb - > {output}) 2> {log}"

# rule bwa_map:
#     input:
#         "data/genome.fa",
#         get_bwa_map_input_fastqs
#     output:
#         "mapped_reads/{sample}.bam"
#     params:
#         rg=r"@RG\tID:{sample}\tSM:{sample}"
#     threads: 8
#     shell:
#         "bwa mem -R '{params.rg}' -t {threads} {input} | samtools view -Sb - > {output}"


# rule bwa_map:
#     input:
#         "data/genome.fa",
#         get_bwa_map_input_fastqs
#     output:
#         "mapped_reads/{sample}.bam"
#     threads: 8
#     shell:
#         "bwa mem -t {threads} {input} | samtools view -Sb - > {output}"

# rule bwa_map:
#     input:
#         "data/genome.fa",
#         "data/samples/{sample}.fastq"
#     output:
#         "mapped_reads/{sample}.bam"
#     threads: 8
#     shell:
#         "bwa mem -t {threads} {input} | samtools view -Sb - > {output}"

rule samtools_sort:
    input:
        "mapped_reads/{sample}.bam"
    output:
        protected("sorted_reads/{sample}.bam")
    shell:
        "samtools sort -T sorted_reads/{wildcards.sample} "
        "-O bam {input} > {output}"

# rule samtools_sort:
#     input:
#         "mapped_reads/{sample}.bam"
#     output:
#         "sorted_reads/{sample}.bam"
#     shell:
#         "samtools sort -T sorted_reads/{wildcards.sample} "
#         "-O bam {input} > {output}"

rule samtools_index:
  input:
      "sorted_reads/{sample}.bam"
  output:
      "sorted_reads/{sample}.bam.bai"
  conda:
      "envs/samtools.yaml"
  shell:
      "samtools index {input}"

# rule samtools_index:
#     input:
#         "sorted_reads/{sample}.bam"
#     output:
#         "sorted_reads/{sample}.bam.bai"
#     shell:
#         "samtools index {input}"

rule bcftools_call:
    input:
        fa="data/genome.fa",
        bam=expand("sorted_reads/{sample}.bam", sample=config["samples"]),
        bai=expand("sorted_reads/{sample}.bam.bai", sample=config["samples"])
    output:
        "calls/all.vcf"
    params:
        rg=config["mutation_rate"]
    log: # Output log of the rule create in a file
        "logs/bcftools_call/all.log" # Log files must contain exactly the same wildcards as the output files
    shell:
        "(bcftools mpileup -f {input.fa} {input.bam} | "
        "bcftools call -P '{params.rg}' -mv - > {output}) 2> {log}"

# rule bcftools_call:
#     input:
#         fa="data/genome.fa",
#         bam=expand("sorted_reads/{sample}.bam", sample=config["samples"]),
#         bai=expand("sorted_reads/{sample}.bam.bai", sample=config["samples"])
#     output:
#         "calls/all.vcf"
#     params:
#         rg=config["mutation_rate"] # Modify here
#     shell:
#         "bcftools mpileup -f {input.fa} {input.bam} | "
#         "bcftools call -P '{params.rg}' -mv - > {output}" # Modify here

# rule bcftools_call:
#     input:
#         fa="data/genome.fa",
#         bam=expand("sorted_reads/{sample}.bam", sample=config["samples"]),
#         bai=expand("sorted_reads/{sample}.bam.bai", sample=config["samples"])
#     output:
#         "calls/all.vcf"
#     shell:
#         "bcftools mpileup -f {input.fa} {input.bam} | "
#         "bcftools call -mv - > {output}"

rule plot_quals:
    input:
        "calls/all.vcf"
    output:
        "plots/quals.svg"
    script:
        "scripts/plot-quals.py"

