# Se prepara la tabla:
setwd("/media/lab204/DATOS/Eva/eomes/ChIPSeq/homologs/")

find_by_ID_name<-function(ID,Names){
  name<-Names$Associated.Gene.Name[Names$Ensembl.Gene.ID==ID][1] ## finds name for ID
  return(name)
}

find_by_ID<-function(ID, X){
  name<-X$V2[X$V1==ID][1] ## finds score for ID
  return(name)
}

biomart<-read.table("HomHXZ_ensg.txt", header = TRUE, sep = "\t", stringsAsFactors = FALSE)
HX<-biomart[(biomart$Xenopus.Ensembl.Gene.ID!="")==TRUE,]
HXZ<-HX[(HX$Zebrafish.Ensembl.Gene.ID!="")==TRUE,]
write.table(HXZ, 'PWHomHXZ.txt', sep="\t", quote = FALSE, col.names = FALSE, row.names = FALSE)
Names<-read.table("H_ID_Name.txt", header = TRUE, sep = "\t", stringsAsFactors = FALSE)
NAM<-lapply(HXZ$Ensembl.Gene.ID, find_by_ID_name, Names)
HXZ$Names<-NAM
