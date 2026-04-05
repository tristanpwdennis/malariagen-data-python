# Curation metadata

Summary statistics used during our sequence QC process are available within each sample set subdirectory, in a file named "sequence_qc_stats.csv". Each file contains the following fields:

- `sample_id` (string) - MalariaGEN sample identifier
- `mean_cov` (float) - mean coverage
- `median_cov` (int) - median coverage
- `modal_cov` (int) - modal coverage
- `mean_cov_{contig}` (float) - mean coverage for a particular contig
- `median_cov_{contig}` (int) - median coverage for a particular contig
- `mode_cov_{contig}` (int) - modal coverage for a particular contig
- `frac_gen_cov` (float) - fraction of the genome covered
- `divergence` (float) - divergence

For further information or queries contact support@malariagen.net.
