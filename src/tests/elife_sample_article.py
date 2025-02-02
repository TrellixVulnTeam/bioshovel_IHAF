import textwrap

xml_file_string = textwrap.dedent('''
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE article PUBLIC "-//NLM//DTD JATS (Z39.96) Journal Archiving and Interchange DTD v1.1d3 20150301//EN" "JATS-archivearticle1.dtd">
<article article-type="research-article" dtd-version="1.1d3" xmlns:mml="http://www.w3.org/1998/Math/MathML" xmlns:xlink="http://www.w3.org/1999/xlink">
 <front>
  <journal-meta>
   <journal-id journal-id-type="nlm-ta">
    elife
   </journal-id>
   <journal-id journal-id-type="hwp">
    eLife
   </journal-id>
   <journal-id journal-id-type="publisher-id">
    eLife
   </journal-id>
   <journal-title-group>
    <journal-title>
     eLife
    </journal-title>
   </journal-title-group>
   <issn pub-type="epub" publication-format="electronic">
    2050-084X
   </issn>
   <publisher>
    <publisher-name>
     eLife Sciences Publications, Ltd
    </publisher-name>
   </publisher>
  </journal-meta>
  <article-meta>
   <article-id pub-id-type="publisher-id">
    13027
   </article-id>
   <article-id pub-id-type="doi">
    10.7554/eLife.13027
   </article-id>
   <article-categories>
    <subj-group subj-group-type="display-channel">
     <subject>
      Research article
     </subject>
    </subj-group>
    <subj-group subj-group-type="heading">
     <subject>
      Biophysics and structural biology
     </subject>
    </subj-group>
   </article-categories>
   <title-group>
    <article-title>
     Atomic structure of the 26S proteasome lid reveals the mechanism of deubiquitinase inhibition
    </article-title>
   </title-group>
   <contrib-group>
    <contrib contrib-type="author" equal-contrib="yes" id="author-46262">
     <name>
      <surname>
       Dambacher
      </surname>
      <given-names>
       Corey M
      </given-names>
     </name>
     <xref ref-type="aff" rid="aff1">
      1
     </xref>
     <xref ref-type="fn" rid="equal-contrib">
      †
     </xref>
     <xref ref-type="fn" rid="con1">
     </xref>
     <xref ref-type="fn" rid="conf1">
     </xref>
    </contrib>
    <contrib contrib-type="author" equal-contrib="yes" id="author-46263">
     <name>
      <surname>
       Worden
      </surname>
      <given-names>
       Evan J
      </given-names>
     </name>
     <xref ref-type="aff" rid="aff2">
      2
     </xref>
     <xref ref-type="aff" rid="aff3">
      3
     </xref>
     <xref ref-type="fn" rid="equal-contrib">
      †
     </xref>
     <xref ref-type="fn" rid="con2">
     </xref>
     <xref ref-type="fn" rid="conf1">
     </xref>
    </contrib>
    <contrib contrib-type="author" equal-contrib="yes" id="author-46264">
     <name>
      <surname>
       Herzik
      </surname>
      <given-names>
       Mark A
      </given-names>
      <suffix>
       Jr.
      </suffix>
     </name>
     <xref ref-type="aff" rid="aff1">
      1
     </xref>
     <xref ref-type="fn" rid="equal-contrib">
      †
     </xref>
     <xref ref-type="fn" rid="con3">
     </xref>
     <xref ref-type="fn" rid="conf1">
     </xref>
    </contrib>
    <contrib contrib-type="author" corresp="yes" id="author-11271">
     <name>
      <surname>
       Martin
      </surname>
      <given-names>
       Andreas
      </given-names>
     </name>
     <xref ref-type="aff" rid="aff2">
      2
     </xref>
     <xref ref-type="aff" rid="aff3">
      3
     </xref>
     <xref ref-type="aff" rid="aff4">
      4
     </xref>
     <xref ref-type="corresp" rid="cor1">
      *
     </xref>
     <xref ref-type="other" rid="par-5">
     </xref>
     <xref ref-type="other" rid="par-6">
     </xref>
     <xref ref-type="fn" rid="con4">
     </xref>
     <xref ref-type="fn" rid="conf1">
     </xref>
    </contrib>
    <contrib contrib-type="author" corresp="yes" id="author-11421">
     <name>
      <surname>
       Lander
      </surname>
      <given-names>
       Gabriel C
      </given-names>
     </name>
     <xref ref-type="aff" rid="aff1">
      1
     </xref>
     <xref ref-type="corresp" rid="cor2">
      *
     </xref>
     <xref ref-type="other" rid="par-1">
     </xref>
     <xref ref-type="other" rid="par-2">
     </xref>
     <xref ref-type="other" rid="par-3">
     </xref>
     <xref ref-type="other" rid="par-4">
     </xref>
     <xref ref-type="fn" rid="con5">
     </xref>
     <xref ref-type="fn" rid="conf1">
     </xref>
    </contrib>
    <aff id="aff1">
     <label>
      1
     </label>
     <institution content-type="dept">
      Department of Integrative Structural and Computational Biology
     </institution>
     ,
     <institution>
      The Scripps Research Institute
     </institution>
     ,
     <addr-line>
      <named-content content-type="city">
       La Jolla
      </named-content>
     </addr-line>
     ,
     <country>
      United States
     </country>
    </aff>
    <aff id="aff2">
     <label>
      2
     </label>
     <institution content-type="dept">
      Department of Molecular and Cell Biology
     </institution>
     ,
     <institution>
      University of California, Berkeley
     </institution>
     ,
     <addr-line>
      <named-content content-type="city">
       Berkeley
      </named-content>
     </addr-line>
     ,
     <country>
      United States
     </country>
    </aff>
    <aff id="aff3">
     <label>
      3
     </label>
     <institution content-type="dept">
      QB3 Institute
     </institution>
     ,
     <institution>
      University of California, Berkeley
     </institution>
     ,
     <addr-line>
      <named-content content-type="city">
       Berkeley
      </named-content>
     </addr-line>
     ,
     <country>
      United States
     </country>
    </aff>
    <aff id="aff4">
     <label>
      4
     </label>
     <institution>
      Howard Hughes Medical Institute, University of California, Berkeley
     </institution>
     ,
     <addr-line>
      <named-content content-type="city">
       Berkeley
      </named-content>
     </addr-line>
     ,
     <country>
      United States
     </country>
    </aff>
   </contrib-group>
   <contrib-group content-type="section">
    <contrib contrib-type="editor">
     <name>
      <surname>
       Scheres
      </surname>
      <given-names>
       Sjors HW
      </given-names>
     </name>
     <role>
      Reviewing editor
     </role>
     <aff id="aff5">
      <institution>
       Medical Research Council
      </institution>
      ,
      <country>
       United Kingdom
      </country>
     </aff>
    </contrib>
   </contrib-group>
   <author-notes>
    <corresp id="cor1">
     <email>
      a.martin@berkeley.edu
     </email>
     (AM);
    </corresp>
    <corresp id="cor2">
     <email>
      glander@scripps.edu
     </email>
     (GCL)
    </corresp>
    <fn fn-type="con" id="equal-contrib">
     <label>
      †
     </label>
     <p>
      These authors contributed equally to this work
     </p>
    </fn>
   </author-notes>
   <pub-date date-type="pub" publication-format="electronic">
    <day>
     08
    </day>
    <month>
     01
    </month>
    <year>
     2016
    </year>
   </pub-date>
   <pub-date pub-type="collection">
    <year>
     2016
    </year>
   </pub-date>
   <volume>
    5
   </volume>
   <elocation-id>
    e13027
   </elocation-id>
   <history>
    <date date-type="received">
     <day>
      13
     </day>
     <month>
      11
     </month>
     <year>
      2015
     </year>
    </date>
    <date date-type="accepted">
     <day>
      07
     </day>
     <month>
      01
     </month>
     <year>
      2016
     </year>
    </date>
   </history>
   <permissions>
    <copyright-statement>
     © 2016, Dambacher et al
    </copyright-statement>
    <copyright-year>
     2016
    </copyright-year>
    <copyright-holder>
     Dambacher et al
    </copyright-holder>
    <license xlink:href="http://creativecommons.org/licenses/by/4.0/">
     <license-p>
      This article is distributed under the terms of the
      <ext-link ext-link-type="uri" xlink:href="http://creativecommons.org/licenses/by/4.0/">
       Creative Commons Attribution License
      </ext-link>
      , which permits unrestricted use and redistribution provided that the original author and source are credited.
     </license-p>
    </license>
   </permissions>
   <self-uri content-type="pdf" xlink:href="elife-13027.pdf">
   </self-uri>
   <abstract>
    <object-id pub-id-type="doi">
     10.7554/eLife.13027.001
    </object-id>
    <p>
     The 26S proteasome is responsible for the selective, ATP-dependent degradation of polyubiquitinated cellular proteins. Removal of ubiquitin chains from targeted substrates at the proteasome is a prerequisite for substrate processing and is accomplished by Rpn11, a deubiquitinase within the ‘lid’ sub-complex. Prior to the lid’s incorporation into the proteasome, Rpn11 deubiquitinase activity is inhibited to prevent unwarranted deubiquitination of polyubiquitinated proteins. Here we present the atomic model of the isolated lid sub-complex, as determined by cryo-electron microscopy at 3.5 Å resolution, revealing how Rpn11 is inhibited through its interaction with a neighboring lid subunit, Rpn5. Through mutagenesis of specific residues, we describe the network of interactions that are required to stabilize this inhibited state. These results provide significant insight into the intricate mechanisms of proteasome assembly, outlining the substantial conformational rearrangements that occur during incorporation of the lid into the 26S holoenzyme, which ultimately activates the deubiquitinase for substrate degradation.
    </p>
    <p>
     <bold>
      DOI:
     </bold>
     <ext-link ext-link-type="doi" xlink:href="10.7554/eLife.13027.001">
      http://dx.doi.org/10.7554/eLife.13027.001
     </ext-link>
    </p>
   </abstract>
   <abstract abstract-type="executive-summary">
    <object-id pub-id-type="doi">
     10.7554/eLife.13027.002
    </object-id>
    <title>
     eLife digest
    </title>
    <p>
     The proteins contained within cells are constantly under scrutiny by a sophisticated “quality control” system that tags damaged or malfunctioning proteins with chains made up of a protein called ubiquitin. These ubiquitin chains serve as markers that target these toxic proteins for destruction by a molecular complex called the proteasome.
    </p>
    <p>
     Removing ubiquitin chains from toxic proteins is a critical step in their degradation by the proteasome. This task is accomplished by an enzyme called a deubiquitinase, whose activity is tightly controlled. However, it was not clear how this enzyme is kept inactive before it is incorporated into the proteasome complex.
    </p>
    <p>
     The deubiquitinase is part of a sub-complex called the “lid”, which attaches to the side of the proteasome. Dambacher, Worden, Herzik et al. used electron microscopy to solve the structure of the lid complex in high detail – so that it was almost possible to view individual atoms. This revealed that the deubiquitinase was in a conformation that was very different from what had previously been observed in fully assembled proteasomes.
    </p>
    <p>
     The structures revealed that within the lid complex, a complicated network of interactions causes the deubiquitinase to be encompassed by neighboring subunits. This prevents the enzyme from interacting with ubiquitin chains. Importantly, this network of interactions appears to be set on a hair-trigger, as mutations that disrupt these interactions cause the deubiquitinase to be activated. As the lid complex integrates into the proteasome, the lid undergoes large-scale structural rearrangements; Dambacher, Worden, Herzik et al. expect that these disrupt the interactions that maintain the deubiquitinase in an inhibited conformation.
    </p>
    <p>
     Due to their ability to regulate the activity of the proteasome, deubiquitinases are becoming increasingly popular drug targets. Therefore, probing how they are activated in more detail will be of great importance to cell biologists and also contribute substantially to biomedical research.
    </p>
    <p>
     <bold>
      DOI:
     </bold>
     <ext-link ext-link-type="doi" xlink:href="10.7554/eLife.13027.002">
      http://dx.doi.org/10.7554/eLife.13027.002
     </ext-link>
    </p>
   </abstract>
   <kwd-group kwd-group-type="author-keywords">
    <title>
     Author Keywords
    </title>
    <kwd>
     proteasome
    </kwd>
    <kwd>
     deubiquitination
    </kwd>
    <kwd>
     cryoEM
    </kwd>
   </kwd-group>
   <kwd-group kwd-group-type="research-organism">
    <title>
     Research Organism
    </title>
    <kwd>
     &lt;i&gt;S. cerevisiae&lt;/i&gt;
    </kwd>
   </kwd-group>
   <funding-group>
    <award-group id="par-1">
     <funding-source>
      <institution-wrap>
       <institution-id institution-id-type="FundRef">
        http://dx.doi.org/10.13039/100001021
       </institution-id>
       <institution>
        Damon Runyon Cancer Research Foundation
       </institution>
      </institution-wrap>
     </funding-source>
     <award-id>
      DFS-#07-13
     </award-id>
     <principal-award-recipient>
      <name>
       <surname>
        Lander
       </surname>
       <given-names>
        Gabriel C
       </given-names>
      </name>
     </principal-award-recipient>
    </award-group>
    <award-group id="par-2">
     <funding-source>
      <institution-wrap>
       <institution-id institution-id-type="FundRef">
        http://dx.doi.org/10.13039/100000875
       </institution-id>
       <institution>
        Pew Charitable Trusts
       </institution>
      </institution-wrap>
     </funding-source>
     <principal-award-recipient>
      <name>
       <surname>
        Lander
       </surname>
       <given-names>
        Gabriel C
       </given-names>
      </name>
     </principal-award-recipient>
    </award-group>
    <award-group id="par-3">
     <funding-source>
      <institution-wrap>
       <institution-id institution-id-type="FundRef">
        http://dx.doi.org/10.13039/100005665
       </institution-id>
       <institution>
        Kinship Foundation
       </institution>
      </institution-wrap>
     </funding-source>
     <principal-award-recipient>
      <name>
       <surname>
        Lander
       </surname>
       <given-names>
        Gabriel C
       </given-names>
      </name>
     </principal-award-recipient>
    </award-group>
    <award-group id="par-4">
     <funding-source>
      <institution-wrap>
       <institution-id institution-id-type="FundRef">
        http://dx.doi.org/10.13039/100000002
       </institution-id>
       <institution>
        National Institutes of Health
       </institution>
      </institution-wrap>
     </funding-source>
     <award-id>
      DP2 EB020402-01
     </award-id>
     <principal-award-recipient>
      <name>
       <surname>
        Lander
       </surname>
       <given-names>
        Gabriel C
       </given-names>
      </name>
     </principal-award-recipient>
    </award-group>
    <award-group id="par-5">
     <funding-source>
      <institution-wrap>
       <institution-id institution-id-type="FundRef">
        http://dx.doi.org/10.13039/100000001
       </institution-id>
       <institution>
        National Science Foundation
       </institution>
      </institution-wrap>
     </funding-source>
     <award-id>
      NSF-MCB-1150288
     </award-id>
     <principal-award-recipient>
      <name>
       <surname>
        Martin
       </surname>
       <given-names>
        Andreas
       </given-names>
      </name>
     </principal-award-recipient>
    </award-group>
    <award-group id="par-6">
     <funding-source>
      <institution-wrap>
       <institution-id institution-id-type="FundRef">
        http://dx.doi.org/10.13039/100000002
       </institution-id>
       <institution>
        National Institutes of Health
       </institution>
      </institution-wrap>
     </funding-source>
     <award-id>
      R01-GM094497
     </award-id>
     <principal-award-recipient>
      <name>
       <surname>
        Martin
       </surname>
       <given-names>
        Andreas
       </given-names>
      </name>
     </principal-award-recipient>
    </award-group>
    <funding-statement>
     The funders had no role in study design, data collection and interpretation, or the decision to submit the work for publication.
    </funding-statement>
   </funding-group>
   <custom-meta-group>
    <custom-meta>
     <meta-name>
      elife-xml-version
     </meta-name>
     <meta-value>
      2.5
     </meta-value>
    </custom-meta>
    <custom-meta specific-use="meta-only">
     <meta-name>
      Author impact statement
     </meta-name>
     <meta-value>
      Within the isolated lid sub-complex of the proteasome, a finely tuned network of interactions maintains the deubiquitinase in an inhibited conformation; dramatic rearrangements of the lid subunits upon incorporation into the holoenzyme lead to the deubiquitinase’s activation.
     </meta-value>
    </custom-meta>
   </custom-meta-group>
  </article-meta>
 </front>
 <body>
  <sec id="s1" sec-type="intro">
   <title>
    Introduction
   </title>
   <p>
    The eukaryotic 26S proteasome is a large multi-enzyme complex that functions as the primary degradation machinery for the selective turnover of aberrant or unneeded proteins within the cell. Proteins targeted for degradation are covalently labeled with polyubiquitin chains, which are recognized and removed by the proteasome (
    <xref ref-type="bibr" rid="bib12">
     Finley, 2009
    </xref>
    ). The barrel-shaped core peptidase complex of the proteasome, which sequesters the proteolytic active sites in an internal chamber (
    <xref ref-type="bibr" rid="bib16">
     Groll et al., 1997
    </xref>
    ), is capped on one or both ends by a regulatory particle that acts as a discriminating gateway for targeted protein substrates (
    <xref ref-type="bibr" rid="bib30">
     Saeki and Tanaka, 2012
    </xref>
    ). The regulatory particle consists of two sub-complexes, known as the ‘base’ and the ‘lid’ (
    <xref ref-type="bibr" rid="bib14">
     Glickman et al., 1998
    </xref>
    ). The base sub-complex contains the AAA+ ATPases Rpt1-Rpt6, which form a heterohexameric ring that drives the mechanical substrate unfolding and translocation of the unstructured polypeptides into the degradation chamber of the core peptidase. Docked on one side of the base is the lid subcomplex, which contains the deubiquitinating enzyme (DUB) Rpn11 that cleaves polyubiquitin chains from targeted substrates as an essential step in proteasomal substrate processing (
    <xref ref-type="bibr" rid="bib4">
     Boehringer et al., 2012
    </xref>
    ).
   </p>
   <p>
    The lid is an asymmetric, ~370 kDa complex that consists of 9 unique subunits (Rpn3, 5, 6, 7, 8, 9, 11, 12, Sem1) and exhibits a characteristic hand-shaped organization similar to that of the eukaryotic initiation factor 3 (eIF3) and the COP9 signalosome (CSN) (
    <xref ref-type="bibr" rid="bib21">
     Lander et al., 2012
    </xref>
    ;
    <xref ref-type="bibr" rid="bib24">
     Lingaraju et al., 2014
    </xref>
    ;
    <xref ref-type="bibr" rid="bib7">
     des Georges et al., 2015
    </xref>
    ). At the center of the lid, six
    <bold>
     P
    </bold>
    roteasome-
    <bold>
     C
    </bold>
    SN-e
    <bold>
     I
    </bold>
    F3 (PCI)-domain containing subunits (Rpn3, 5, 6, 7, 9, 12) interact via their winged-helix motifs to form a horseshoe-shaped scaffold. The amino-terminal domains of these 6 subunits extend radially like fingers from the central PCI horseshoe. The essential deubiquitinase Rpn11 is positioned in the ‘palm’ of the hand-shaped lid. Rpn11 is an
    <bold>
     M
    </bold>
    pr1-
    <bold>
     P
    </bold>
    ad1
    <bold>
     N
    </bold>
    -terminal (MPN)-domain containing metalloprotease of the
    <bold>
     JA
    </bold>
    B1/
    <bold>
     M
    </bold>
    PN/
    <bold>
     M
    </bold>
    OV34 (JAMM) family and forms a heterodimer with an enzymatically inactive MPN-subunit, Rpn8. With the exception of Sem1, a small 87-residue subunit located at the interface of the N-terminal domains of Rpn3 and Rpn7 (
    <xref ref-type="bibr" rid="bib5">
     Bohn et al., 2013
    </xref>
    ), all lid subunits contain conserved C-terminal helices that assemble into a large bundle positioned next to the MPN heterodimer of Rpn11/Rpn8 in the palm of the complex (
    <xref ref-type="bibr" rid="bib2">
     Beck et al., 2012
    </xref>
    ).
   </p>
   <p>
    Previous crystallographic and biochemical studies have focused on the mechanism of Rpn11, which acts as a highly promiscuous DUB to remove ubiquitins from the wide variety of substrates during their translocation into the proteasome, likely by cleaving the isopeptide bond between the substrate lysine and the first ubiquitin moiety of the attached ubiquitin chain (
    <xref ref-type="bibr" rid="bib40">
     Worden et al., 2014
    </xref>
    ;
    <xref ref-type="bibr" rid="bib28">
     Pathare et al., 2014
    </xref>
    ). The Rpn11/Rpn8 heterodimer is active in isolation (
    <xref ref-type="bibr" rid="bib40">
     Worden et al., 2014
    </xref>
    ), but is significantly inhibited in the context of the lid sub-complex and regains robust DUB activity in the assembled 26S proteasome (
    <xref ref-type="bibr" rid="bib38">
     Verma et al., 2002
    </xref>
    ;
    <xref ref-type="bibr" rid="bib41">
     Yao and Cohen, 2002
    </xref>
    ). The isolated Rpn11/Rpn8 heterodimer is not present at considerable levels in the cell, whereas the presence of the lid and its assembly intermediates containing Rpn11/Rpn8 have been previously observed and characterized (
    <xref ref-type="bibr" rid="bib35">
     Tomko and Hochstrasser, 2011
    </xref>
    ). The inhibition of Rpn11 activity in the isolated lid and its assembly intermediates might therefore be important to prevent spurious deubiquitination of proteins in the cell, given the high promiscuity of this DUB. It has been suggested that interactions with Rpn5 are possibly involved in Rpn11 inhibition in the isolated lid (
    <xref ref-type="bibr" rid="bib21">
     Lander et al., 2012
    </xref>
    ), but the specifics of this regulation and the mechanism by which Rpn11 is activated upon incorporation into the holoenzyme remain elusive (
    <xref ref-type="bibr" rid="bib38">
     Verma et al., 2002
    </xref>
    ;
    <xref ref-type="bibr" rid="bib21">
     Lander et al., 2012
    </xref>
    ;
    <xref ref-type="bibr" rid="bib41">
     Yao and Cohen, 2002
    </xref>
    ).
   </p>
   <p>
    Here, we present an atomic model of the isolated lid sub-complex of the yeast proteasome, as determined by cryo-electron microscopy (cryoEM) (
    <xref ref-type="fig" rid="fig1">
     Figure 1A–C
    </xref>
    ,
    <xref ref-type="table" rid="tbl1">
     Table 1
    </xref>
    ,
    <xref ref-type="fig" rid="fig1s1">
     Figure 1—figures supplements 1
    </xref>
    –
    <xref ref-type="fig" rid="fig1s4">
     4
    </xref>
    ), revealing the molecular mechanism for direct inhibition of the DUB active site, as well as Rpn11 activation through extensive conformational changes that occur during lid incorporation into the 26S holoenzyme.
    <fig-group>
     <fig id="fig1" position="float">
      <object-id pub-id-type="doi">
       10.7554/eLife.13027.003
      </object-id>
      <label>
       Figure 1.
      </label>
      <caption>
       <title>
        Architecture of the isolated proteasome lid sub-complex.
       </title>
       <p>
        (
        <bold>
         A
        </bold>
        ) The segmented 3.5 Å resolution cryo-EM density is shown at a low isocontour level, with each subunit colored differently. Rpn3 is shown in orange, Rpn5 in light blue, Rpn6 in yellow, Rpn7 in purple, Rpn8 in red, Rpn9 in magenta, Rpn11 in green, Rpn12 in light green, and Sem1 in tan. This coloring scheme is maintained throughout all figures. (
        <bold>
         B
        </bold>
        ) The unsegmented cryoEM density is shown at a higher isocontour level (in gold) to demonstrate the molecular details observable in the reconstruction (~3Å in certain regions). The lower isocontour level used for the segmented map is overlaid as a silhouette. (
        <bold>
         C
        </bold>
        ) The atomic model of the proteasome lid is depicted using a ribbon representation, with each subunit colored according to the segmentation shown in A. The central location of the six PCI domains is illustrated by a gray shadow underneath the structure. (
        <bold>
         D
        </bold>
        ) The PCI domains form a horseshoe, held together by an 18-stranded β-sheet. (
        <bold>
         E
        </bold>
        ) Close-up of the helical bundle and the MPN heterodimer.
       </p>
       <p>
        <bold>
         DOI:
        </bold>
        <ext-link ext-link-type="doi" xlink:href="10.7554/eLife.13027.003">
         http://dx.doi.org/10.7554/eLife.13027.003
        </ext-link>
       </p>
      </caption>
      <graphic xlink:href="elife-13027-fig1">
      </graphic>
     </fig>
     <fig id="fig1s1" position="float" specific-use="child-fig">
      <object-id pub-id-type="doi">
       10.7554/eLife.13027.004
      </object-id>
      <label>
       Figure 1—figure supplement 1.
      </label>
      <caption>
       <title>
        CryoEM data collection.
       </title>
       <p>
        (A) A representative cryo-electron micrograph (scale bar = 100 nm) after whole-frame alignment. (B) Reference-free 2D class averages of frozen-hydrated particles, showing a variety of different projection views of the lid complex. (C) A Fourier transform of the representative micrograph, with a simulated CTF estimated by CTFFind3 overlaid on the right half of the image. Thon rings are clearly observed beyond 4Å (white circle). (D) A 1-dimentional plot showing the correlation of the experimental CTF (blue) and the estimated CTF (black). Images having a correlation of the of greater than 50% beyond 4 Å resolution were used for subsequent processing. (E) Per-frame B-factors (B
        <sub>
         f
        </sub>
        , top) and intercepts (C
        <sub>
         f
        </sub>
        , bottom). (F) Per-frame weighting of spatial frequencies, based on the B
        <sub>
         f
        </sub>
        and C
        <sub>
         f
        </sub>
        estimates shown in e. First and last frames are colored in yellow, and the frame with the least negative relative B
        <sub>
         f
        </sub>
        is colored in orange (frame 5). Frames 4–16 are the major contributors to the high-resolution spatial frequencies.
       </p>
       <p>
        <bold>
         DOI:
        </bold>
        <ext-link ext-link-type="doi" xlink:href="10.7554/eLife.13027.004">
         http://dx.doi.org/10.7554/eLife.13027.004
        </ext-link>
       </p>
      </caption>
      <graphic xlink:href="elife-13027-fig1-figsupp1">
      </graphic>
     </fig>
     <fig id="fig1s2" position="float" specific-use="child-fig">
      <object-id pub-id-type="doi">
       10.7554/eLife.13027.005
      </object-id>
      <label>
       Figure 1—figure supplement 2.
      </label>
      <caption>
       <title>
        Single particle analysis of the lid complex.
       </title>
       <p>
        A total of 254,113 particles were extracted from micrographs, scaled by a factor of 0.25, and subjected to 3D classification into 8 classes in RELION. The particle coordinates corresponding to the four highest resolution classes that showed density for all lid components were re-centered, based on the translations determined from 3D classification. These coordinates were used to extract 139,561 unbinned particles for 3D refinement with RELION, which yielded a reconstruction of 4.4 Å. After correcting for particle motion and electron beam damage (particle polishing), the resolution was improved to 4.1 Å. A 3D mask surrounding the most structurally stable regions of the map (the PCI domains, the MPN heterodimer, and the helical bundle) was generated, and used in an alignment-free 3D classification of the data into 3 classes. The 109,396 particles contributing to the highest resolution 3D class were used for further 3D refinement in RELION without applying a mask, yielding a 3.6 Å structure. Continued refinement of these alignment parameters using the same 3D mask that was applied earlier improved the resolution of the central regions of the structure by 0.1 Å.
       </p>
       <p>
        <bold>
         DOI:
        </bold>
        <ext-link ext-link-type="doi" xlink:href="10.7554/eLife.13027.005">
         http://dx.doi.org/10.7554/eLife.13027.005
        </ext-link>
       </p>
      </caption>
      <graphic xlink:href="elife-13027-fig1-figsupp2">
      </graphic>
     </fig>
     <fig id="fig1s3" position="float" specific-use="child-fig">
      <object-id pub-id-type="doi">
       10.7554/eLife.13027.006
      </object-id>
      <label>
       Figure 1—figure supplement 3.
      </label>
      <caption>
       <title>
        Resolution assessment of the reconstructions.
       </title>
       <p>
        (
        <bold>
         A
        </bold>
        ) 3D angular distribution plot, shown from three orthogonal angles of the reconstruction. The diameter and color saturation of the spheres increases with occupancy of particles at a given Euler angle. (B) Fourier Shell Correlation plots of lid reconstructions at different stages of processing. (C) The final map is shown at two contour levels, colored according to a local resolution estimation using Bsoft (
        <xref ref-type="bibr" rid="bib18">
         Heymann and Belnap, 2007
        </xref>
        ). A lower contour level (left) shows the more disordered regions, while the higher contour level (right) shows that regions of the map were resolved to 3 Å resolution. An outline of the lower contour is overlaid on top of the images on the right for reference.
       </p>
       <p>
        <bold>
         DOI:
        </bold>
        <ext-link ext-link-type="doi" xlink:href="10.7554/eLife.13027.006">
         http://dx.doi.org/10.7554/eLife.13027.006
        </ext-link>
       </p>
      </caption>
      <graphic xlink:href="elife-13027-fig1-figsupp3">
      </graphic>
     </fig>
     <fig id="fig1s4" position="float" specific-use="child-fig">
      <object-id pub-id-type="doi">
       10.7554/eLife.13027.007
      </object-id>
      <label>
       Figure 1—figure supplement 4.
      </label>
      <caption>
       <title>
        Atomic modeling of the lid sub-complex.
       </title>
       <p>
        (A) The 5 top-scoring models are shown, with each subunit colored differently. Close-up views of the cryo-EM density in the regions within the black boxes are shown in (B–D). Side chains in the helical bundle (B, C) were well-resolved, and the 5 models were largely consistent in these regions. At the periphery of the complex, however, structural features were less well-resolved and the models are less consistent. (E) The atomic model is colored according to B-values, which are largely consistent with the local resolution map shown in
        <xref ref-type="fig" rid="fig1s3">
         Figure 1—figure supplement 3
        </xref>
        . Blue regions correspond to B-values of ~50 Å
        <sup>
         2
        </sup>
        , while red regions correspond to B-factors of ~300 Å
        <sup>
         2
        </sup>
        . (F) The FSCs between the top-scoring atomic model refined against one of the half-maps and the final 3.5 Å map (dashed line) and the two independently refined half maps (light and dark solid lines) are shown. For comparison, the FSC between the independently refined half maps is also plotted (dotted line). The overlap of the curves in the high spatial frequencies indicate that the model was not over-fitted.
       </p>
       <p>
        <bold>
         DOI:
        </bold>
        <ext-link ext-link-type="doi" xlink:href="10.7554/eLife.13027.007">
         http://dx.doi.org/10.7554/eLife.13027.007
        </ext-link>
       </p>
      </caption>
      <graphic xlink:href="elife-13027-fig1-figsupp4">
      </graphic>
     </fig>
     <fig id="fig1s5" position="float" specific-use="child-fig">
      <object-id pub-id-type="doi">
       10.7554/eLife.13027.008
      </object-id>
      <label>
       Figure 1—figure supplement 5.
      </label>
      <caption>
       <title>
        Subunits of the yeast 26S proteasome lid sub-complex.
       </title>
       <p>
        The well-ordered cryo-EM densities for the 9 lid subunits are shown as transparent surfaces, with the atomic models shown as ribbons. Side-chain density is clearly visible for the C-terminal helices of the PCI-containing domains, and the MPN-containing subunits are well-resolved throughout. The cryoEM density for the PCI-containing subunits become less ordered near the N-terminus of these subunits, and is only visible at lower contour levels.
       </p>
       <p>
        <bold>
         DOI:
        </bold>
        <ext-link ext-link-type="doi" xlink:href="10.7554/eLife.13027.008">
         http://dx.doi.org/10.7554/eLife.13027.008
        </ext-link>
       </p>
      </caption>
      <graphic xlink:href="elife-13027-fig1-figsupp5">
      </graphic>
     </fig>
     <fig id="fig1s6" position="float" specific-use="child-fig">
      <object-id pub-id-type="doi">
       10.7554/eLife.13027.009
      </object-id>
      <label>
       Figure 1—figure supplement 6.
      </label>
      <caption>
       <title>
        Comparison of PCI horseshoes in different complexes.
       </title>
       <p>
        Shown are ribbon representations of the PCI horseshoes of (from left to right) the unincorporated lid, the incorporated lid (PDB ID: 4CR2) (
        <xref ref-type="bibr" rid="bib37">
         Unverdorben et al., 2014
        </xref>
        ), the COP9 signalosome (PDB ID: 4D18) (
        <xref ref-type="bibr" rid="bib24">
         Lingaraju et al., 2014
        </xref>
        ), and eIF3 (PDB ID: 5A5T) (
        <xref ref-type="bibr" rid="bib7">
         des Georges et al., 2015
        </xref>
        ). The PCI horseshoes all adopt a staircase arrangement, and the pseudo-helical pitch for each horseshoe was determined, as well as the radius of the helix. The PCI horseshoe in the unincorporated lid complex (left) is more open, and less planar than that of the incorporated lid. The helical parameters and diameter of the PCI horseshoe in the incorporated lid closely resembles that of the COP9 Signalosome. Of the four PCI horseshoes, the arrangement of eIF3 is most open and least helical in arrangement.
       </p>
       <p>
        <bold>
         DOI:
        </bold>
        <ext-link ext-link-type="doi" xlink:href="10.7554/eLife.13027.009">
         http://dx.doi.org/10.7554/eLife.13027.009
        </ext-link>
       </p>
      </caption>
      <graphic xlink:href="elife-13027-fig1-figsupp6">
      </graphic>
     </fig>
     <fig id="fig1s7" position="float" specific-use="child-fig">
      <object-id pub-id-type="doi">
       10.7554/eLife.13027.010
      </object-id>
      <label>
       Figure 1—figure supplement 7.
      </label>
      <caption>
       <title>
        Interactions of the helical bundle with surrounding lid components.
       </title>
       <p>
        The helical bundle (which is emphasized by a semi-transparent Gaussian-filtered surface) only makes significant interactions with the PCI domain of Rpn9 (magenta-colored ribbon). There also appears to be a contact established between the C-terminus of the Rpn6 helix (yellow) and the N-terminal domain of Rpn3 (orange). The cryoEM density is shown in the lower left panel, showing the putative Rpn3-Rpn6 interaction.
       </p>
       <p>
        <bold>
         DOI:
        </bold>
        <ext-link ext-link-type="doi" xlink:href="10.7554/eLife.13027.010">
         http://dx.doi.org/10.7554/eLife.13027.010
        </ext-link>
       </p>
      </caption>
      <graphic xlink:href="elife-13027-fig1-figsupp7">
      </graphic>
     </fig>
    </fig-group>
    <table-wrap id="tbl1" position="float">
     <object-id pub-id-type="doi">
      10.7554/eLife.13027.011
     </object-id>
     <label>
      Table 1.
     </label>
     <caption>
      <p>
       CryoEM data collection, processing, and modeling
      </p>
      <p>
       <bold>
        DOI:
       </bold>
       <ext-link ext-link-type="doi" xlink:href="10.7554/eLife.13027.011">
        http://dx.doi.org/10.7554/eLife.13027.011
       </ext-link>
      </p>
     </caption>
     <table frame="hsides" rules="groups">
      <thead>
       <tr>
        <th colspan="4">
         Data collection
        </th>
       </tr>
      </thead>
      <tbody>
       <tr>
        <td>
        </td>
        <td colspan="2">
         Microscope
        </td>
        <td>
         FEI Titan Krios
        </td>
       </tr>
       <tr>
        <td>
        </td>
        <td colspan="2">
         Camera
        </td>
        <td>
         Gatan K2 Summit
        </td>
       </tr>
       <tr>
        <td>
        </td>
        <td colspan="2">
         Voltage
        </td>
        <td>
         300 keV
        </td>
       </tr>
       <tr>
        <td>
        </td>
        <td colspan="2">
         Magnification
        </td>
        <td>
         22,500
        </td>
       </tr>
       <tr>
        <td>
        </td>
        <td colspan="2">
         Pixel size
        </td>
        <td>
         1.31 Å (0.655 Å, super-resolution)
        </td>
       </tr>
       <tr>
        <td>
        </td>
        <td colspan="2">
         Dose rate
        </td>
        <td>
         9.9 e
         <sup>
          -
         </sup>
         /pixel/s
        </td>
       </tr>
       <tr>
        <td>
        </td>
        <td colspan="2">
         Cumulative electron dose
        </td>
        <td>
         43.8 e
         <sup>
          -
         </sup>
         /Å
         <sup>
          2
         </sup>
        </td>
       </tr>
       <tr>
        <td>
        </td>
        <td colspan="2">
         Exposure
        </td>
        <td>
         7.6 s
        </td>
       </tr>
       <tr>
        <td>
        </td>
        <td colspan="2">
         Number of frames
        </td>
        <td>
         38
        </td>
       </tr>
       <tr>
        <td>
        </td>
        <td colspan="2">
         Defocus range
        </td>
        <td>
         1.5–3.5 µm
        </td>
       </tr>
       <tr>
        <td>
        </td>
        <td colspan="2">
         Micrographs collected
        </td>
        <td>
         3,432
        </td>
       </tr>
       <tr>
        <td>
        </td>
        <td colspan="2">
         Acquisition software
        </td>
        <td>
         Leginon (
         <xref ref-type="bibr" rid="bib34">
          Suloway et al., 2005
         </xref>
         )
        </td>
       </tr>
       <tr>
        <td colspan="4">
         Image Processing
        </td>
       </tr>
       <tr>
        <td>
        </td>
        <td colspan="2">
         Preprocessing package
        </td>
        <td>
         Appion (
         <xref ref-type="bibr" rid="bib22">
          Lander et al., 2009
         </xref>
         )
        </td>
       </tr>
       <tr>
        <td>
        </td>
        <td colspan="2">
         Frame alignment software
        </td>
        <td>
         MotionCorr (whole image) (
         <xref ref-type="bibr" rid="bib23">
          Li et al., 2013
         </xref>
         )
        </td>
       </tr>
       <tr>
        <td>
        </td>
        <td colspan="2">
         CTF estimation software
        </td>
        <td>
         CTFFind3 (
         <xref ref-type="bibr" rid="bib26">
          Mindell and Grigorieff, 2003
         </xref>
         )
        </td>
       </tr>
       <tr>
        <td>
        </td>
        <td colspan="2">
         CTF cutoff criterion
        </td>
        <td>
         4 Å at 0.5 confidence
        </td>
       </tr>
       <tr>
        <td>
        </td>
        <td colspan="2">
         Particle picking software
        </td>
        <td>
         FindEM (
         <xref ref-type="bibr" rid="bib29">
          Roseman, 2004
         </xref>
         )
        </td>
       </tr>
       <tr>
        <td>
        </td>
        <td colspan="2">
         Micrographs used
        </td>
        <td>
         3,365
        </td>
       </tr>
       <tr>
        <td>
        </td>
        <td colspan="2">
         Particles selected
        </td>
        <td>
         254,112
        </td>
       </tr>
       <tr>
        <td colspan="4">
         Reconstruction
        </td>
       </tr>
       <tr>
        <td>
        </td>
        <td colspan="2">
         Software
        </td>
        <td>
         RELION 1.3 (
         <xref ref-type="bibr" rid="bib32">
          Scheres, 2012
         </xref>
         )
        </td>
       </tr>
       <tr>
        <td>
        </td>
        <td colspan="2">
         Particles contributed
        </td>
        <td>
         109,396
        </td>
       </tr>
       <tr>
        <td>
        </td>
        <td colspan="2">
         Rotational accuracy
        </td>
        <td>
         1.392 degrees
        </td>
       </tr>
       <tr>
        <td>
        </td>
        <td colspan="2">
         Translational accuracy
        </td>
        <td>
         0.671 pixels
        </td>
       </tr>
       <tr>
        <td>
        </td>
        <td colspan="2">
         B-factor applied
        </td>
        <td>
         -75.9
        </td>
       </tr>
       <tr>
        <td>
        </td>
        <td colspan="2">
         Final resolution @ FSC 0.143
        </td>
        <td>
         3.5 Å
        </td>
       </tr>
       <tr>
        <td colspan="4">
         Model building and Refinement
        </td>
       </tr>
       <tr>
        <td>
        </td>
        <td colspan="2">
         Number of residues
        </td>
        <td>
         2743 (86%)
        </td>
       </tr>
       <tr>
        <td>
        </td>
        <td colspan="2">
         Map CC (whole unit cell)
        </td>
        <td>
         0.758
        </td>
       </tr>
       <tr>
        <td>
        </td>
        <td colspan="2">
         Map CC (all atoms)
        </td>
        <td>
         0.853
        </td>
       </tr>
       <tr>
        <td>
        </td>
        <td colspan="2">
         R.M.S deviations
        </td>
        <td>
        </td>
       </tr>
       <tr>
        <td colspan="2">
        </td>
        <td>
         Bond length (Å)
        </td>
        <td>
         0.02
        </td>
       </tr>
       <tr>
        <td colspan="2">
        </td>
        <td>
         Bond angle (˚°)
        </td>
        <td>
         1.15
        </td>
       </tr>
       <tr>
        <td>
        </td>
        <td colspan="2">
         Ramachandran plot stats
        </td>
        <td>
        </td>
       </tr>
       <tr>
        <td colspan="2">
        </td>
        <td>
         Preferred
        </td>
        <td>
         2646 (96.47%)
        </td>
       </tr>
       <tr>
        <td colspan="2">
        </td>
        <td>
         Allowed
        </td>
        <td>
         92 (3.35%)
        </td>
       </tr>
       <tr>
        <td colspan="2">
        </td>
        <td>
         Outlier
        </td>
        <td>
         5 (0.18%)
        </td>
       </tr>
       <tr>
        <td>
        </td>
        <td colspan="2">
         Rotamer outliers
        </td>
        <td>
         5 (0.20%)
        </td>
       </tr>
       <tr>
        <td>
        </td>
        <td colspan="2">
         C-beta deviations
        </td>
        <td>
         0 (0.00%)
        </td>
       </tr>
      </tbody>
     </table>
    </table-wrap>
   </p>
  </sec>
  <sec id="s2" sec-type="results|discussion">
   <title>
    Results and discussion
   </title>
   <sec id="s2-1">
    <title>
     Lid architecture
    </title>
    <p>
     Our cryo-EM reconstruction of the isolated lid shows that the MPN heterodimer, PCI horseshoe, and helical bundle together comprise a rigid substructure that contains regions resolved to ~3 Å resolution (
     <xref ref-type="fig" rid="fig1">
      Figure 1B
     </xref>
     ,
     <xref ref-type="fig" rid="fig1s3">
      Figure 1—figure supplements 3
     </xref>
     –
     <xref ref-type="fig" rid="fig1s5">
      5
     </xref>
     ). The N-terminal portions of the PCI-domain containing subunits progressively decrease in resolution as they extend toward the periphery of the complex, likely due to intrinsic flexibility (
     <xref ref-type="fig" rid="fig1s3">
      Figure 1—figure supplements 3C
     </xref>
     ,
     <xref ref-type="fig" rid="fig1s5">
      5
     </xref>
     ). The 3D reconstructions of the fully assembled lid and the lid lacking Rpn12 (
     <xref ref-type="fig" rid="fig1s2">
      Figure 1—figure supplement 2
     </xref>
     , top row, third reconstruction) show that the N-terminal portions of Rpn6 and Rpn5 are fully extended, and the MPN heterodimer and helical bundle adopt identical orientations in both structures. These findings contradict a recent crosslinking study (
     <xref ref-type="bibr" rid="bib36">
      Tomko et al., 2015
     </xref>
     ) suggesting that incorporation of Rpn12 during lid assembly induces a large-scale rearrangement of the MPN dimer and the transition of the N-terminal portion of Rpn6 from an inward-folded state to an extended conformation that allows binding to the base. Further structural studies will therefore be required to better understand how Rpn12 incorporation affects lid binding to the base and core subcomplexes.
    </p>
    <p>
     We found that the six PCI winged-helix domains associate into a continuous 18-stranded β-sheet, forming an incomplete right-handed spiral at the center of the lid sub-complex (
     <xref ref-type="fig" rid="fig1">
      Figure 1C, D
     </xref>
     ,
     <xref ref-type="fig" rid="fig1s6">
      Figure 1—figure supplement 6
     </xref>
     ). This organization was also observed in the crystal structure of CSN, although the PCI horseshoe assembly of the isolated lid has a wider and steeper spiral (
     <xref ref-type="fig" rid="fig1s6">
      Figure 1—figure supplement 6
     </xref>
     ). Recently, a similar succession of β-strands was shown for the PCI domains in eIF3 (
     <xref ref-type="bibr" rid="bib7">
      des Georges et al., 2015
     </xref>
     ), but its domain organization is significantly more open and deviates from the spiral configuration observed in the proteasome lid and CSN (
     <xref ref-type="fig" rid="fig1s6">
      Figure 1—figure supplement 6
     </xref>
     ). The significant conformational differences between the horseshoes of the lid, CSN, and eIF3 indicate that the PCI-domain assembly allows for substantial flexibility, while simultaneously serving as an organizational scaffold at the center of the complex.
    </p>
    <p>
     The C-terminal helices of all lid subunits (except Sem1) assemble into a well-defined helical bundle that is centrally positioned within the lid sub-complex, adjacent to the PCI horseshoe and the MPN heterodimer (
     <xref ref-type="fig" rid="fig1">
      Figure 1E
     </xref>
     ,
     <xref ref-type="fig" rid="fig1s7">
      Figure 1—figure supplement 7
     </xref>
     ). Our cryoEM reconstruction contains sufficient structural detail to generate a complete atomic model of this helical bundle, providing an accurate depiction of the extensive inter-helical interactions. Furthermore, we were able to precisely assign the register of several helices that could not be unambiguously positioned in earlier lower-resolution models of this bundle (
     <xref ref-type="bibr" rid="bib2">
      Beck et al., 2012
     </xref>
     ;
     <xref ref-type="bibr" rid="bib37">
      Unverdorben et al., 2014
     </xref>
     ;
     <xref ref-type="bibr" rid="bib10">
      Estrin et al., 2013
     </xref>
     ). Our structure shows that Rpn8 and Rpn11 are the only subunits that contribute multiple helices to the bundle and together contact all other subunits within the helical assembly. Notably, Rpn8 is the largest contributor to the bundle, which is consistent with previous biochemical work showing that the Rpn8 C-terminal helices are more critical for lid assembly than those of other subunits (
     <xref ref-type="bibr" rid="bib10">
      Estrin et al., 2013
     </xref>
     ). The PCI horseshoe and MPN heterodimer are individually tethered to the bundle via short loops, but make only few direct surface contacts with the bundle. The cryoEM map also shows that the bundle’s position in the isolated lid is likely stabilized by interactions between α-helix 5 (residues 186–215) of Rpn8 and the PCI domain of Rpn9 at one end of the bundle, and between the C-terminus of Rpn6 and the N-terminus of Rpn3 at the opposite end (
     <xref ref-type="fig" rid="fig1">
      Figure 1E
     </xref>
     ,
     <xref ref-type="fig" rid="fig1s7">
      Figure 1—figure supplement 7
     </xref>
     ).
    </p>
    <p>
     The cryoEM reconstruction of the isolated lid allowed us to examine the structural elements involved in regulating Rpn11 DUB activity. Notably, within the isolated lid, the Rpn11/Rpn8 heterodimer is positioned in a previously unobserved orientation relative to the other subunits, stably associated within the palm of the hand-shaped complex via two primary interfaces with the
     <bold>
      t
     </bold>
     etratrico
     <bold>
      p
     </bold>
     eptide
     <bold>
      r
     </bold>
     epeat (TPR) domain of Rpn5 and the α-solenoid of Rpn9 (
     <xref ref-type="fig" rid="fig2">
      Figure 2A–C
     </xref>
     ). The resulting organization produces the basis for Rpn11 DUB inhibition in the isolated lid.
     <fig-group>
      <fig id="fig2" position="float">
       <object-id pub-id-type="doi">
        10.7554/eLife.13027.012
       </object-id>
       <label>
        Figure 2.
       </label>
       <caption>
        <title>
         The MPN heterodimer interacts extensively with Rpn5 and Rpn9.
        </title>
        <p>
         (
         <bold>
          A
         </bold>
         ) Side view of the lid sub-complex shows that the MPN heterodimer (Rpn8 in red, Rpn11 in green) interacts closely with the Rpn5 (blue) and Rpn9 (lavender) subunits. Side-chain interactions likely responsible for maintaining the MPN heterodimer in this configuration are shown in detail in panels (
         <bold>
          B
         </bold>
         ) and (
         <bold>
          C
         </bold>
         ). Residues that were mutated to alanine for deubiquitination assays are labeled in black. (
         <bold>
          D
         </bold>
         ) Measurements of fluorescence increase upon Rpn11-mediated cleavage of ubiquitin-AMC are shown for three lid mutants relative to the wild-type lid. (
         <bold>
          E
         </bold>
         ) Ubiquitin-AMC cleavage rates show activation of Rpn11 in the lid upon mutation of residues within Rpn5 and Rpn8.
        </p>
        <p>
         <bold>
          DOI:
         </bold>
         <ext-link ext-link-type="doi" xlink:href="10.7554/eLife.13027.012">
          http://dx.doi.org/10.7554/eLife.13027.012
         </ext-link>
        </p>
       </caption>
       <graphic xlink:href="elife-13027-fig2">
       </graphic>
      </fig>
      <fig id="fig2s1" position="float" specific-use="child-fig">
       <object-id pub-id-type="doi">
        10.7554/eLife.13027.013
       </object-id>
       <label>
        Figure 2—figure supplement 1.
       </label>
       <caption>
        <title>
         Buried surface area between the MPN heterodimer and Rpn9 and Rpn5.
        </title>
        <p>
         An MSMS surface was generated from the atomic model of the lid sub-complex, and the buried surface area was calculated for the interfaces of Rpn8 and Rpn9 (colored yellow), and Rpn11 and Rpn5 (colored magenta). The Rpn11-Rpn5 interface is the largest site of interaction between the all of the PCI-containing subunits and the MPN-heterodimer, with a buried surface area of ~631 Å
         <sup>
          2
         </sup>
         . The Rpn8-Rpn9 interface is the next largest, with a buried surface area of ~452 Å
         <sup>
          2
         </sup>
         .
        </p>
        <p>
         <bold>
          DOI:
         </bold>
         <ext-link ext-link-type="doi" xlink:href="10.7554/eLife.13027.013">
          http://dx.doi.org/10.7554/eLife.13027.013
         </ext-link>
        </p>
       </caption>
       <graphic xlink:href="elife-13027-fig2-figsupp1">
       </graphic>
      </fig>
      <fig id="fig2s2" position="float" specific-use="child-fig">
       <object-id pub-id-type="doi">
        10.7554/eLife.13027.014
       </object-id>
       <label>
        Figure 2—figure supplement 2.
       </label>
       <caption>
        <title>
         Interface mutations in Rpn5 and Rpn9 release the MPN dimer from its inhibited conformation.
        </title>
        <p>
         Negative stain EM analysis was performed on the lid mutants. On the left are 2D class averages depicting the canonical hand-shaped arrangement of the lid sub-complex from the front and top views. On the right are 3D reconstructions of the lid, showing the organization of the PCI horseshoe, as well as the position of the Rpn11/Rpn8 heterodimer (red and green) relative to Rpn9 (pink) and Rpn5 (blue). The 2D and 3D analyses of the wild type particles show that the MPN heterodimer is closely associated with the Rpn5 and Rpn9 subunits (top row). The mutants, however, show that the while overall organization of the PCI-containing subunits are preserved, the MPN dimer is released from its position in the palm of the lid sub-complex. In the 2D class averages, the detached MPN dimer can be identified as an additional density that is not observed in the WT class average (indicated by a yellow arrow). In the 3D reconstructions, the WT structure shows the MPN dimer (green and red) are connected to Rpn5 (blue) and Rpn9 (purple). The density corresponding to the dimer in all the mutants is clearly detached from Rpn5 and Rpn9. The MPN dimer within the Rpn5 (Y273A) (bottom row) had such an increased level of flexibility, that the dimer itself is poorly resolved.
        </p>
        <p>
         <bold>
          DOI:
         </bold>
         <ext-link ext-link-type="doi" xlink:href="10.7554/eLife.13027.014">
          http://dx.doi.org/10.7554/eLife.13027.014
         </ext-link>
        </p>
       </caption>
       <graphic xlink:href="elife-13027-fig2-figsupp2">
       </graphic>
      </fig>
     </fig-group>
    </p>
   </sec>
   <sec id="s2-2">
    <title>
     Rpn5 occludes the Rpn11 active site
    </title>
    <p>
     We first probed the contacts between Rpn11 and Rpn5 for their contributions to Rpn11 inhibition in the isolated lid, as this interface is more extensive (total buried surface area of ~630 Å
     <sup>
      2
     </sup>
     ) than all other subunit interactions with the MPN heterodimer (
     <xref ref-type="fig" rid="fig2s1">
      Figure 2—figure supplement 1
     </xref>
     ). Importantly, the N-terminal region of α-helix 13 in Rpn5 (residues 275–285) is nestled against the end of Rpn11’s catalytic groove, with several residues from Rpn5 directly contacting loops that surround Rpn11’s catalytic Zn
     <sup>
      2+
     </sup>
     ion (
     <xref ref-type="fig" rid="fig2">
      Figure 2C
     </xref>
     ). To test the functional importance of these contacts, we generated Rpn5-mutated lid variants and compared their ubiquitin-7-amino-4-methylcoumarin (Ub-AMC) cleavage rate with that of wild-type lid and the isolated Rpn11/Rpn8 dimer. Under our assay conditions, Rpn11 activity within the isolated lid is 5-fold lower compared to the free Rpn11/Rpn8 dimer. In the loop preceding α-helix 13 of Rpn5, Tyr273 is in an orientation that enables hydrophobic interactions with Rpn11 Phe114, located in a loop near the active site (
     <xref ref-type="fig" rid="fig2">
      Figure 2C
     </xref>
     ). Mutation of this Rpn5 residue (Y273A) increased Rpn11 activity to 61% of the isolated Rpn11/Rpn8 dimer (
     <xref ref-type="fig" rid="fig2">
      Figure 2D–E
     </xref>
     ), suggesting that Tyr273 aids in stabilizing Rpn11 in its inhibited conformation.
    </p>
    <p>
     Rpn5 residues His282 and Lys283 directly interact with the backbone atoms of two loops near the Rpn11 active site, and their substitution with alanine increased Rpn11 activity to 31% and 41% of the free MPN heterodimer, respectively (
     <xref ref-type="fig" rid="fig2">
      Figure 2C, E
     </xref>
     ). The effects of these mutations were additive, as the Rpn5 (H282A,K283A) double-mutant lid exhibited 51% DUB activity compared to the free MPN heterodimer (
     <xref ref-type="fig" rid="fig2">
      Figure 2E
     </xref>
     ). Structural analysis of the lid containing the Rpn5 (Y273A) or the Rpn5 (H282A,K283A) double-mutant by negative-stain EM shows that the Rpn11/Rpn8 heterodimer is released from its inhibitory conformation, while the overall organization of the PCI-containing subunits is identical to that of the isolated wild-type lid complex (
     <xref ref-type="fig" rid="fig2s2">
      Figure 2—figure supplement 2
     </xref>
     ). Together, these activating mutations support a model wherein Tyr273, His282, and Lys283 of Rpn5 all stabilize the association of α-helix 13 with the Rpn11 active site, generating a structural barrier that blocks substrates from accessing the catalytic groove.
    </p>
    <p>
     In addition to preventing access to the Rpn11 active site by steric occlusion, the close proximity of Rpn5 in the isolated lid further blocks DUB activity through interaction with the catalytic Zn
     <sup>
      2+
     </sup>
     (
     <xref ref-type="fig" rid="fig3">
      Figure 3A
     </xref>
     ). Two histidines (His109 and His111) and an aspartate (Asp112) coordinate the Zn
     <sup>
      2+
     </sup>
     within the Rpn11 active site, a configuration that is preserved in all JAMM metalloenzymes (
     <xref ref-type="bibr" rid="bib20">
      Komander et al., 2009
     </xref>
     ). This geometry allows for interaction with a fourth ligand, as Zn
     <sup>
      2+
     </sup>
     is usually tetrahedrally coordinated in proteins (
     <xref ref-type="bibr" rid="bib13">
      Gerke and Moss, 2002
     </xref>
     ). Despite the close proximity of Rpn5’s α-helix 13 to the Rpn11 active site, intermolecular distances preclude direct interaction of any Rpn5 residues with the catalytic Zn
     <sup>
      2+
     </sup>
     . The Rpn5 residue that is closest to the zinc is Asn275, which is notably oriented with its carboxamide group directed towards the Rpn11 active site. Mutation of Asn275 to alanine increases Rpn11 DUB activity in the isolated lid to 51% of the isolated MPN heterodimer (
     <xref ref-type="fig" rid="fig2">
      Figure 2E
     </xref>
     ), and negative-stain EM of this lid mutant shows the Rpn11/Rpn8 heterodimer detached from its inhibited conformation (
     <xref ref-type="fig" rid="fig2s2">
      Figure 2—figure supplement 2
     </xref>
     ).
     <fig-group>
      <fig id="fig3" position="float">
       <object-id pub-id-type="doi">
        10.7554/eLife.13027.015
       </object-id>
       <label>
        Figure 3.
       </label>
       <caption>
        <title>
         The Rpn11 active site is inhibited in the isolated lid.
        </title>
        <p>
         (
         <bold>
          A
         </bold>
         ) The catalytic Zn
         <sup>
          2+
         </sup>
         (gray sphere) within the Rpn11 active site (green ribbon) is coordinated by three residues from Rpn11, and a water molecule acts as a fourth ligand, likely mediated by Asn275 from the neighboring Rpn5 subunit (blue). The cryoEM density in this region is shown as a mesh. (
         <bold>
          B
         </bold>
         ) Comparison of the Rpn11 active sites from the isolated Rpn11/Rpn8 heterodimer crystal structure (PDB ID: 4O8X, purple) and isolated lid (green) shows that the two structures are nearly superimposable. (
         <bold>
          C
         </bold>
         ) A di-ubiquitin substrate (tan) was modeled into the active site and shown as a transparent surface rendering. The modeled substrate severely clashes with the locked Rpn11 Ins-1 loop and Rpn5. (
         <bold>
          D
         </bold>
         ) In CSN, a Glu within the Ins-1 loop provides a fourth point of coordination for the Zn
         <sup>
          2+
         </sup>
         ion. (
         <bold>
          E
         </bold>
         ) Similar to CSN, an AMSH mutant utilizes an Asp from the Ins-1 loop to establish tetrahedral coordination of the catalytic Zn
         <sup>
          2+
         </sup>
         .
        </p>
        <p>
         <bold>
          DOI:
         </bold>
         <ext-link ext-link-type="doi" xlink:href="10.7554/eLife.13027.015">
          http://dx.doi.org/10.7554/eLife.13027.015
         </ext-link>
        </p>
       </caption>
       <graphic xlink:href="elife-13027-fig3">
       </graphic>
      </fig>
      <fig id="fig3s1" position="float" specific-use="child-fig">
       <object-id pub-id-type="doi">
        10.7554/eLife.13027.016
       </object-id>
       <label>
        Figure 3—figure supplement 1.
       </label>
       <caption>
        <title>
         Water-mediated tetrahedral coordination of active site Zn
         <sup>
          2+
         </sup>
         in Rpn11 and AMSH orthologue Sst2.
        </title>
        <p>
         The deubiquitinase active site of isolated lid’s Rpn11 subunit (left) and an Sst2 mutant (PDB ID: 4MSM) (
         <xref ref-type="bibr" rid="bib33">
          Shrestha et al., 2014
         </xref>
         ) (right) are shown, depicting the coordination of the catalytic Zn
         <sup>
          2+
         </sup>
         (gray sphere) by three active site residues, and a catalytic water molecule (red sphere). In both structures, the water molecule is hydrogen-bonded to a residue from an additional component. In the lid, the catalytic water in the Rpn11 active site is bound to N275 from Rpn5, and in the Sst2 mutant, the water interacts with the carboxylate group of Gly76 from a cleaved Ubiquitin.
        </p>
        <p>
         <bold>
          DOI:
         </bold>
         <ext-link ext-link-type="doi" xlink:href="10.7554/eLife.13027.016">
          http://dx.doi.org/10.7554/eLife.13027.016
         </ext-link>
        </p>
       </caption>
       <graphic xlink:href="elife-13027-fig3-figsupp1">
       </graphic>
      </fig>
      <fig id="fig3s2" position="float" specific-use="child-fig">
       <object-id pub-id-type="doi">
        10.7554/eLife.13027.017
       </object-id>
       <label>
        Figure 3—figure supplement 2.
       </label>
       <caption>
        <title>
         Relative B-values of the Rpn11 Ins-1 loop in the isolated Rpn11/Rpn8 heterodimer and in the isolated lid sub-complex.
        </title>
        <p>
         A ribbon representation of the Rpn11 Ins-1 loop in the crystal structure of the isolated Rpn11/Rpn8 heterodimer and within the isolated lid sub-complex is colored according to the B-factor values (blue = low B-factor, red = high B-value). Notably, the Ins-1 loop in the isolated MPN heterodimer has significantly higher average B-values than the rest of Rpn11, while the B-values of the Ins-1 loop in the cryo-EM structure of the lid sub-complex are slightly lower than the average B-factor value of the Rpn11 subunit. This suggests that the Ins-1 loop is stabilized in this conformation within the lid assembly.
        </p>
        <p>
         <bold>
          DOI:
         </bold>
         <ext-link ext-link-type="doi" xlink:href="10.7554/eLife.13027.017">
          http://dx.doi.org/10.7554/eLife.13027.017
         </ext-link>
        </p>
       </caption>
       <graphic xlink:href="elife-13027-fig3-figsupp2">
       </graphic>
      </fig>
     </fig-group>
    </p>
    <p>
     Although Rpn5 Asn275 is not within range to directly bind the catalytic Zn
     <sup>
      2+
     </sup>
     (~5 Å from the Zn
     <sup>
      2+
     </sup>
     to Nδ1 of Asn275), the cryo-EM density in the Rpn11 active site shows connectivity between Asn275 and the catalytic Zn
     <sup>
      2+
     </sup>
     (
     <xref ref-type="fig" rid="fig3">
      Figure 3A
     </xref>
     ), potentially corresponding to a coordinated water molecule. Indeed, a Zn-associated water molecule is known to play a key role in the peptide hydrolysis mechanism of Zn-dependent proteases and has been observed in the crystal structures of Rpn11 (
     <xref ref-type="bibr" rid="bib40">
      Worden et al., 2014
     </xref>
     ;
     <xref ref-type="bibr" rid="bib28">
      Pathare et al., 2014
     </xref>
     ) and related DUBs of the JAMM family, such as AMSH (
     <xref ref-type="bibr" rid="bib33">
      Shrestha et al., 2014
     </xref>
     ;
     <xref ref-type="bibr" rid="bib6">
      Davies et al., 2011
     </xref>
     ). Furthermore, the co-crystal structure of the AMSH ortholog Sst2 bound to a post-cleavage ubiquitin fragment shows that the carboxylate of ubiquitin Gly76 forms a hydrogen bond with the catalytic water (
     <xref ref-type="bibr" rid="bib33">
      Shrestha et al., 2014
     </xref>
     ) in the same manner as Rpn5 Asn275 in the isolated lid (
     <xref ref-type="fig" rid="fig3s1">
      Figure 3—figure supplement 1
     </xref>
     ). While the Sst2 structure presents a snapshot of the transient substrate cleavage product prior to its departure from the active site, the positioning of Rpn5 Asn275 establishes a stable tetrahedral coordination of the Zn
     <sup>
      2+
     </sup>
     ion via this catalytic water molecule, inhibiting isopeptidase activity of Rpn11 in the isolated lid sub-complex.
    </p>
   </sec>
   <sec id="s2-3">
    <title>
     Rpn9 stabilizes the inhibited MPN heterodimer
    </title>
    <p>
     The other major interface involved in stabilizing the DUB-inhibited conformation of the isolated lid is found between Rpn8 and Rpn9, and involves a 5-residue loop connecting α-helix 8 (residues 143–159) and α-helix 9 (residues 165–182) of Rpn9. While the buried surface area of this interface (~450 Å
     <sup>
      2
     </sup>
     ) is smaller than the Rpn5-Rpn11 interface (
     <xref ref-type="fig" rid="fig2s1">
      Figure 2—figure supplement 1
     </xref>
     ), mutagenesis of the interface residues shows that these contacts also contribute significantly to maintaining the sequestered position of the MPN heterodimer within the palm of the isolated lid sub-complex.
    </p>
    <p>
     Our atomic model suggests that Rpn8 Gln115 interacts with the backbone atoms of Rpn9 Ile163 (
     <xref ref-type="fig" rid="fig2">
      Figure 2B
     </xref>
     ), and upon mutation of Gln115 to alanine, we observed elevated Rpn11 activity that was 33% of isolated MPN levels. Furthermore, two lysine residues in Rpn8, Lys86 and Lys88, are likely involved in electrostatic interactions with Rpn9 Asp158, which is located at the C-terminal end of α-helix 8 (
     <xref ref-type="fig" rid="fig2">
      Figure 2B
     </xref>
     ). Mutation of Lys86 and Lys88 to alanine in Rpn8 of the isolated lid increases Rpn11 activity to 33% and 45% of the free MPN-heterodimer levels, respectively. The double mutant Rpn8 (K86A,K88A) was additive, stimulating Rpn11 activity to about 60% of the isolated MPN heterodimer. As with the Rpn5 (H282A,K283A) double mutant lid, negative-stain analysis of the Rpn8 (K86A,K88A) double mutant revealed that disruption of the Rpn8-Rpn9 interface releases the MPN dimer from its inhibited conformation (
     <xref ref-type="fig" rid="fig2s2">
      Figure 2—figure supplement 2
     </xref>
     ).
    </p>
    <p>
     Combined with the structural data, our mutational analyses of the MPN-dimer contacts with Rpn5 and Rpn9 suggest that DUB inhibition requires establishment of a finely tuned network of interactions and perturbation of this system at any of the identified contact points disrupts the inhibitory conformation of the MPN dimer within the isolated lid sub-complex.
    </p>
   </sec>
   <sec id="s2-4">
    <title>
     The Ins-1 loop blocks the active site
    </title>
    <p>
     Common structural motifs present in many members of the MPN family are the two insertion loops, Ins-1 and Ins-2, which have been suggested to be involved in orienting ubiquitin chains for cleavage (
     <xref ref-type="bibr" rid="bib31">
      Sato et al., 2008
     </xref>
     ). In Rpn11, Ins-1 is required for catalysis and has been proposed to play a structural role in DUB activity by engaging and positioning the C-terminus of the ubiquitin substrate for hydrolysis (
     <xref ref-type="bibr" rid="bib40">
      Worden et al., 2014
     </xref>
     ). Flexibility of this loop suggests that it may regulate access to the DUB active site by switching between different conformational states. Upon ubiquitin binding to Rpn11, the Ins-1 loop may first open up to allow the ubiquitin C-terminus to enter the catalytic groove and then switch to a conformation that stabilizes the isopeptide bond for hydrolysis. Structures of the isolated Rpn11/Rpn8 dimer show the Ins-1 loop in a ‘closed’ conformation (
     <xref ref-type="bibr" rid="bib40">
      Worden et al., 2014
     </xref>
     ;
     <xref ref-type="bibr" rid="bib28">
      Pathare et al., 2014
     </xref>
     ), which is also observed in EM reconstructions of proteasomes that are actively processing a protein substrate (
     <xref ref-type="bibr" rid="bib37">
      Unverdorben et al., 2014
     </xref>
     ;
     <xref ref-type="bibr" rid="bib25">
      Matyskiela et al., 2013
     </xref>
     ). Interestingly, in the context of the isolated lid, the Ins-1 loop appears to be locked in this closed state through interactions with the neighboring Rpn5 subunit (
     <xref ref-type="fig" rid="fig2">
      Figures 2B
     </xref>
     ,
     <xref ref-type="fig" rid="fig3">
      3B
     </xref>
     ). In particular, the amino group of Rpn5 Lys283 interacts with the Ser74 carbonyl of Ins-1 (
     <xref ref-type="fig" rid="fig2">
      Figure 2C
     </xref>
     ), and introducing the Rpn5 K283A mutation in the isolated lid results in a significant increase in Rpn11 DUB activity, as indicated above.
    </p>
    <p>
     While the Ins-1 loop in the free Rpn11/Rpn8 heterodimer exhibited markedly elevated B-values (
     <xref ref-type="bibr" rid="bib40">
      Worden et al., 2014
     </xref>
     ;
     <xref ref-type="bibr" rid="bib28">
      Pathare et al., 2014
     </xref>
     ), the Rpn11 Ins-1 loop within the isolated lid has lower B-values than the average for all modeled Rpn11 atoms (
     <xref ref-type="fig" rid="fig3s2">
      Figure 3—figure supplement 2
     </xref>
     ). These data suggest that the Ins-1 loop is locked in a closed conformation through contact with neighboring residues and is unable to switch to the ‘open’ state required for substrate access to the active site. The combined effects of the tetrahedral coordination of the catalytic Zn
     <sup>
      2+
     </sup>
     by Asn275 (
     <xref ref-type="fig" rid="fig3">
      Figure 3A
     </xref>
     ), the steric hindrance imposed by Rpn5’s α-helix 13 in the Rpn11 catalytic groove (
     <xref ref-type="fig" rid="fig3">
      Figure 3C
     </xref>
     ), and the obstruction of the DUB active site by the Ins-1 loop result in robust DUB inhibition.
    </p>
    <p>
     Interestingly, the proposed mechanism for auto-inhibition of the catalytically active MPN subunit in CSN, Csn5, also involves tetrahedral coordination of the active-site Zn
     <sup>
      2+
     </sup>
     . However, the fourth ligand in Csn5 is not provided by a neighboring subunit, but intramolecularly by the Ins-1 loop that thereby gets stabilized in a closed conformation (
     <xref ref-type="bibr" rid="bib24">
      Lingaraju et al., 2014
     </xref>
     ) (
     <xref ref-type="fig" rid="fig3">
      Figure 3D
     </xref>
     ). A similar scenario is also observed for a mutant AMSH construct (PDB ID: 3RZV) that utilizes a nearby Asp within the Ins-1 loop to complete the tetrahedral geometry (
     <xref ref-type="bibr" rid="bib33">
      Shrestha et al., 2014
     </xref>
     ) (
     <xref ref-type="fig" rid="fig3">
      Figure 3E
     </xref>
     ).
    </p>
   </sec>
   <sec id="s2-5">
    <title>
     Incorporation of the lid into the 26S holoenzyme
    </title>
    <p>
     Upon incorporation into the 26S proteasome, the lid undergoes major conformational changes that involve the PCI-assembly, the helical bundle, and especially the MPN heterodimer. To visualize these rearrangements, we compared the atomic coordinates of the isolated lid sub-complex to the previously determined pseudo-atomic model of the lid in the context of the assembled proteasome (PDB ID: 4CR2) (
     <xref ref-type="bibr" rid="bib37">
      Unverdorben et al., 2014
     </xref>
     ) (
     <xref ref-type="fig" rid="fig4">
      Figure 4
     </xref>
     and
     <xref ref-type="other" rid="video1">
      Video 1
     </xref>
     ). Lid binding to the base and core sub-complexes causes the PCI horseshoe to constrict, decreasing in radius by ~3 Å, and adopt a more planar conformation that closely resembles the reported architecture of the CSN (
     <xref ref-type="bibr" rid="bib24">
      Lingaraju et al., 2014
     </xref>
     ) (
     <xref ref-type="fig" rid="fig4">
      Figure 4
     </xref>
     ,
     <xref ref-type="fig" rid="fig1s6">
      Figure 1—figure supplement 6
     </xref>
     ). As a result, Rpn3, Rpn7 and Rpn12, comprising one half of the PCI horseshoe, undergo considerable rotation toward the center of the regulatory particle, where Rpn3 and Rpn12 bind the scaffolding subunit Rpn2, while Rpn7 contacts the AAA+ ATPase subunits Rpt3 and Rpt6. By comparison, the other half of the PCI horseshoe, consisting of Rpn9, Rpn5 and Rpn6, goes through a much less pronounced conformational change. The N-terminal α-solenoid domain of Rpn9 extends toward the N-terminal coiled coil of Rpt4 and Rpt5, generating the binding site for the ubiquitin receptor Rpn10, and the highly flexible TPR segment of Rpn5 becomes stabilized through contact with the ATPase ring and the core peptidase. The N-terminal α-solenoid domain of Rpn6 also accommodates interactions with the ATPase ring and core peptidase by rotating ~34º° around its long axis (
     <xref ref-type="fig" rid="fig4s1">
      Figure 4—figure supplement 1
     </xref>
     ).
     <fig-group>
      <fig id="fig4" position="float">
       <object-id pub-id-type="doi">
        10.7554/eLife.13027.018
       </object-id>
       <label>
        Figure 4.
       </label>
       <caption>
        <title>
         The lid sub-complex undergoes a dramatic reorganization upon incorporation to the 26S holoenzyme.
        </title>
        <p>
         Motions associated with lid incorporation are shown from three orthogonal views. Top panels correspond to the isolated lid, while bottom panels represent the proteasome-incorporated lid. Atomic models of the lid subunits were used to generate semi-transparent Gaussian filtered surfaces for visualization. For clarity, the helical bundle, which moves as a rigid body, is shown as a single surface. Sem1 is not shown. The base and core peptidase components are depicted as shadows to not occlude details of the lid rearrangement. Notable rearrangements include: a 90° rotation of the MPN dimer away from the inhibited conformation, movement of Rpn3, 7, and 12 away from Rpn5, 6, and 9, constriction of the PCI horseshoe, and an overall closure of the lid sub-complex around the regulatory particle.
        </p>
        <p>
         <bold>
          DOI:
         </bold>
         <ext-link ext-link-type="doi" xlink:href="10.7554/eLife.13027.018">
          http://dx.doi.org/10.7554/eLife.13027.018
         </ext-link>
        </p>
       </caption>
       <graphic xlink:href="elife-13027-fig4">
       </graphic>
      </fig>
      <fig id="fig4s1" position="float" specific-use="child-fig">
       <object-id pub-id-type="doi">
        10.7554/eLife.13027.019
       </object-id>
       <label>
        Figure 4—figure supplement 1.
       </label>
       <caption>
        <title>
         The Rpn6 α-solenoid domain rotates during incorporation into the holoenzyme.
        </title>
        <p>
         The N-terminal α-solenoid domain rotates ~34° (calculated using DynDom [
         <xref ref-type="bibr" rid="bib17">
          Hayward and Berendsen, 1998
         </xref>
         ]) during incorporation of the lid into the holoenzyme. The PCI domain of the two conformations were aligned, and the overlay of these structures illustrates the solenoid movement, shown from the side and down the axis of rotation. The Rpn6 subunit in the isolated lid sub-complex is colored using a rainbow scheme, with residues at the N-terminus colored blue, and progressing through the color spectrum to red for C-terminal residues. The Rpn6 conformation in the incorporated lid is shown in transparent gray.
        </p>
        <p>
         <bold>
          DOI:
         </bold>
         <ext-link ext-link-type="doi" xlink:href="10.7554/eLife.13027.019">
          http://dx.doi.org/10.7554/eLife.13027.019
         </ext-link>
        </p>
       </caption>
       <graphic xlink:href="elife-13027-fig4-figsupp1">
       </graphic>
      </fig>
      <fig id="fig4s2" position="float" specific-use="child-fig">
       <object-id pub-id-type="doi">
        10.7554/eLife.13027.020
       </object-id>
       <label>
        Figure 4—figure supplement 2.
       </label>
       <caption>
        <title>
         Rpn11’s bundle helix binds to the N-ring of the holoenzyme ATPase.
        </title>
        <p>
         Upon incorporation into the holoenzyme, a short helix from Rpn11 within the helical bundle interacts with the N-ring of the ATPase. This interaction may aid in stabilizing the lid’s position at the side of the regulatory particle.
        </p>
        <p>
         <bold>
          DOI:
         </bold>
         <ext-link ext-link-type="doi" xlink:href="10.7554/eLife.13027.020">
          http://dx.doi.org/10.7554/eLife.13027.020
         </ext-link>
        </p>
       </caption>
       <graphic xlink:href="elife-13027-fig4-figsupp2">
       </graphic>
      </fig>
      <fig id="fig4s3" position="float" specific-use="child-fig">
       <object-id pub-id-type="doi">
        10.7554/eLife.13027.021
       </object-id>
       <label>
        Figure 4—figure supplement 3.
       </label>
       <caption>
        <title>
         Lid incorporation activates Rpn11.
        </title>
        <p>
         (A) Rpn11 activation during proteasome incorporation monitored by ubiquitin-AMC hydrolysis. Fluorescence time courses for the isolated WT lid and Rpn11 (AxA) lid are shown in blue and red, respectively. Background DUB activity of proteasomes reconstituted with Rpn11 (AxA) lid is shown in green, and the activity of proteasomes reconstituted with WT lid is shown in orange. The difference between the time courses for proteasomes reconstituted with WT and Rpn11 (AxA) lid corresponds to Rpn11-dependent DUB activity. (B) Quantification of the ubiquitin-AMC cleavage activities for WT and Rpn11 (AxA) proteasomes shown in a. (
         <bold>
          C
         </bold>
         ) Normalized Ubiquitin-AMC hydrolysis activity of Rpn11-containing complexes in isolation (grey bars) and background-corrected activity of Rpn11 in proteasomes reconstituted with different lid variants (dark grey bars). Error bars in b and c correspond to 1 standard deviation of the data (n = 3).
        </p>
        <p>
         <bold>
          DOI:
         </bold>
         <ext-link ext-link-type="doi" xlink:href="10.7554/eLife.13027.021">
          http://dx.doi.org/10.7554/eLife.13027.021
         </ext-link>
        </p>
       </caption>
       <graphic xlink:href="elife-13027-fig4-figsupp3">
       </graphic>
      </fig>
     </fig-group>
     <media content-type="glencoe play-in-place height-250 width-310" id="video1" mime-subtype="mp4" mimetype="video" xlink:href="elife13027v001.mp4">
      <object-id pub-id-type="doi">
       10.7554/eLife.13027.022
      </object-id>
      <label>
       Video 1.
      </label>
      <caption>
       <title>
        Lid subunit rearrangements that occur during incorporation into the 26S holoenzyme.
       </title>
       <p>
        The atomic model of the isolated lid is interpolated into the pseudo-atomic model of the 26S holoenzyme (
        <xref ref-type="bibr" rid="bib37">
         Unverdorben et al., 2014
        </xref>
        ), showing the motions associated with lid incorporation.
       </p>
       <p>
        <bold>
         DOI:
        </bold>
        <ext-link ext-link-type="doi" xlink:href="10.7554/eLife.13027.022">
         http://dx.doi.org/10.7554/eLife.13027.022
        </ext-link>
       </p>
      </caption>
     </media>
    </p>
    <p>
     The extensive rearrangements of the PCI-containing subunits upon interaction with base and core may also trigger movements of the helical bundle toward the ATPase ring of the base (
     <xref ref-type="fig" rid="fig1">
      Figures 1A, B
     </xref>
     ,
     <xref ref-type="fig" rid="fig2">
      2A
     </xref>
     , and
     <xref ref-type="fig" rid="fig4">
      4
     </xref>
     ). Because the bundle is connected to the PCI horseshoe through flexible loops, it can move as a single unit, ultimately adopting an orientation in the 26S holoenzyme that is more perpendicular to the hand-shaped arrangement of the PCI subunits. Both in the isolated and incorporated lid, the helical bundle contacts the N-terminal domain of Rpn3, albeit through different interfaces. That the association between these two components is maintained during lid incorporation suggests that movement of the Rpn3/7/12 unit influences the positioning of the bundle (
     <xref ref-type="fig" rid="fig4">
      Figure 4
     </xref>
     and
     <xref ref-type="other" rid="video1">
      Video 1
     </xref>
     ). The final orientation of the helical bundle within the regulatory particle is likely also dictated by an extensive interaction between α-helix 6 of Rpn11 (residues 263–272) and the N-terminal domain ring of the ATPase subunits in the base (
     <xref ref-type="fig" rid="fig4s2">
      Figure 4—figure supplement 2
     </xref>
     ).
    </p>
    <p>
     The most pronounced conformational rearrangement of the lid involves the Rpn11/Rpn8 MPN-domain heterodimer. Upon lid incorporation, the Rpn11/Rpn8 dimer undergoes a dramatic 90º° rotation, moving from its inhibited state in the palm of the isolated lid to a highly extended conformation over the central substrate-translocation channel in the 26S holoenzyme (
     <xref ref-type="fig" rid="fig4">
      Figure 4
     </xref>
     ). The inhibited conformation of the Rpn11/Rpn8 heterodimer in the isolated lid appears to be metastable, as mutations in either the Rpn5 or Rpn9 contact surfaces lead to release of the dimer. In fact, the extended conformation of the Rpn11/Rpn8 dimer in the proteasome is similar to its conformation in our DUB-activating lid mutants (
     <xref ref-type="fig" rid="fig2s2">
      Figure 2—figure supplement 2
     </xref>
     ). During lid incorporation, it is likely that the conformational changes occurring in the PCI subunits upon their interactions with the core and base distort the Rpn11-Rpn5 and Rpn8-Rpn9 contact sites and release the Rpn11/Rpn8 dimer from its inhibited state. To assess the extent of Rpn11 activation upon lid incorporation, we compared Ub-AMC hydrolysis activity for Rpn11 in the isolated lid versus the assembled 26S proteasome. Incorporation of wild-type lid stimulated Rpn11 DUB activity to 150% of the isolated Rpn11/Rpn8 dimer levels. This hyperstimulation of Rpn11 in the proteasome may originate from an alternative Ins-1 loop conformation that is stabilized by the neighboring Rpt4/Rpt5 coiled coil. Rpn11 activity in lid sub-complexes that contain Rpn5 (Y273A), Rpn5 (N275A), or Rpn8 (K86A,K88A) mutations was also stimulated upon proteasome incorporation, although to a lower level than with the wild-type lid (
     <xref ref-type="fig" rid="fig4s3">
      Figure 4—figure supplement 3
     </xref>
     ). None of the mutations are involved in interfaces between subunits in the proteasome holoenzyme, and we speculate that the slightly lower DUB activity of the reconstituted mutant proteasomes originates from an interference with normal lid incorporation due to a prematurely released MPN dimer. Interestingly, lid sub-complexes where Rpn11 lacked Ins-2 were completely deficient in Rpn11 stimulation upon incorporation into holoenzyme (
     <xref ref-type="fig" rid="fig4s3">
      Figure 4—figure supplement 3C
     </xref>
     ), even though Rpn11 activity was unaffected by Ins-2 deletion in the isolated lid (
     <xref ref-type="fig" rid="fig2">
      Figure 2E
     </xref>
     ). The Ins-2 region of Rpn11 is known to interact with the scaffolding subunit Rpn2 of the base and likely stabilizes the Rpn11/Rpn8 dimer in the extended conformation.
    </p>
    <p>
     In summary, our structural and functional data suggest that during lid incorporation, the MPN-domain heterodimer loses its stabilizing interactions with Rpn5 and Rpn9, and extends out toward the center of the regulatory particle, leading to Rpn11 activation. This extended conformation enables the Rpn11 Ins-2 loop to interact with Rpn2, which likely aids in positioning the DUB active site above the entrance to the AAA+ ATPase ring for highly regulated deubiquitination of protein substrates during translocation.
    </p>
   </sec>
   <sec id="s2-6">
    <title>
     Conclusions
    </title>
    <p>
     The primary function of the lid sub-complex is to house the isopeptidase Rpn11, an enzyme that is central to proteasomal substrate degradation. While earlier structural and biochemical work described the role of the lid scaffold in positioning Rpn11 and facilitating its activity in the context of the assembled proteasome holoenzyme, we illustrate here how interactions of the Rpn11/Rpn8 dimer with other lid subunits block premature DUB activity in the unincorporated lid assembly. Our atomic model of the isolated lid subcomplex showcases the dramatic conformational gymnastics undergone by this important component of the proteasome during incorporation into the regulatory particle and, while the molecular communication involved in promoting this massive reorganization is still an active area of structural and biochemical research, our work here has resolved an important mystery surrounding DUB inhibition and activation during proteasome assembly.
    </p>
   </sec>
  </sec>
  <sec id="s3" sec-type="materials|methods">
   <title>
    Materials and methods
   </title>
   <sec id="s3-1">
    <title>
     Protein purification
    </title>
    <p>
     Expression and purification of mutant and wild-type recombinant yeast proteasome lid complex was carried out in
     <italic>
      E. coli
     </italic>
     as described previously, with minor modifications (
     <xref ref-type="bibr" rid="bib21">
      Lander et al., 2012
     </xref>
     ). Briefly,
     <italic>
      E. coli
     </italic>
     BL21-star (DE3) cells containing the recombinant lid expression system (pETDuet-1 Rpn5, FLAG-Rpn6, Rpn8, Rpn9, 6xHis-Rpn11], pCOLADuet-1 [Rpn3, Rpn7, Rpn12] and pACYCDuet-1[Sem1, Hsp90) were grown at 37°C in 6 liters of terrific broth (Novagen) supplemented with 150µM ZnCl
     <sub>
      2
     </sub>
     . At OD
     <sub>
      600
     </sub>
     = 1.0, the temperature was reduced to 18°C and, at OD
     <sub>
      600
     </sub>
     = 1.5 lid, expression was induced overnight with 1 mM isopropyl-β-D-thiogalactopyranoside. After centrifugation, cell pellets were re-suspended in lid buffer (60 mM HEPES, pH8.0, 100 mM NaCl, 100 mM KCl, 10% Glycerol, 1 mM DTT) supplemented with protease inhibitors (Aprotinin, Pepstatin, Leupeptin, PMSF), 2mg/ml lysozyme, and bezonase. All purification steps were performed at 4°C. Cells were lysed by sonication and clarified by centrifugation at 16,000g for 30 min. Clarified lysate was incubated with anti-FLAG M2 resin (Sigma-Aldrich), washed with lid buffer and eluted with lid buffer supplemented with 0.15mg/ml 3x-FLAG peptide. FLAG eluate was concentrated to ~500 μl in a 30,000 MWCO spin concentrator (Amicon) and further purified by size-exclusion chromatography on a Superose 6 column (GE Healthcare) that was pre-equilibrated in lid buffer. Peak fractions were concentrated and stored at -80°C. Purification of core particle, Rpn10, Rpn11/Rpn8 MPN-domain dimer and recombinant base was performed as described previously (
     <xref ref-type="bibr" rid="bib21">
      Lander et al., 2012
     </xref>
     ;
     <xref ref-type="bibr" rid="bib40">
      Worden et al., 2014
     </xref>
     ;
     <xref ref-type="bibr" rid="bib3">
      Beckwith et al., 2013
     </xref>
     ).
    </p>
   </sec>
   <sec id="s3-2">
    <title>
     Rpn11 activity assay
    </title>
    <p>
     All Ubiquitin-AMC cleavage experiments were performed at 30°C in lid buffer. Because Rpn11’s Km for various ubiquitin substrates ranges from ~20 to ~300 μM, we assayed our WT and mutant lid variants at a constant, sub-Km Ubiquitin-AMC concentration. For all lid variants and the Rpn11/Rpn8 MPN-domain dimer, 500 nM enzyme was incubated with 2.5 μM Ubiquitin-AMC (Boston Biochem), and Rpn11-catalyzed ubiquitin cleavage was monitored by the increase in AMC fluorescence (Ex: 360 nm, Em: 435 nm) using a QuantaMaster spectrofluorometer (PTI). The slopes of individual time traces were translated to initial cleavage rates using a standard curve for ubiquitin-AMC (ranging from 0.5–2.5 μM) that had been completely cleaved by the DUB Yuh1. Ubiquitin-AMC cleavage rates for all variants were measured in triplicate except for WT lid, Rpn11/Rpn8 dimer, Rpn5 (H282A, K283A) and Rpn8 (Q115A), where n = 11, n = 6, n = 4, and n = 4, respectively.
    </p>
   </sec>
   <sec id="s3-3">
    <title>
     Rpn11 activation upon lid incorporation
    </title>
    <p>
     Proteasomes were reconstituted in vitro with lid as the limiting component by mixing 250 nM lid, 375 nM core particle, 750 nM base and 1 μM Rpn10 in reconstitution buffer (60 mM HEPES, pH7.6, 100 mM NaCl, 100 mM KCl, 10% glycerol, 10 mM MgCl
     <sub>
      2
     </sub>
     , 1 mM DTT, 0.5 mM ATP) that contained an ATP-regeneration system (5 mM ATP, 16 mM creatine phosphate, 6 μg/ml creatine phosphokinase). Deubiquitination reactions were initiated by the addition of 2.5 μM ubiquitin-AMC and monitored by the increase in AMC fluorescence (Ex: 360 nm, Em: 435 nm) using a QuantaMaster spectrofluorometer (PTI). A low level background DUB activity co-purified with our yeast core particle. To subtract this background activity, we reconstituted proteasomes as described above, but with a lid variant containing Rpn11 active-site mutations that abolish zinc binding (Rpn11 [AxA]). The background DUB activity of Rpn11 (AxA) proteasomes was subtracted from the DUB activity of proteasomes reconstituted with WT Rpn11 to get the DUB activity that was specifically contributed by Rpn11. To directly compare the activity of proteasome-incorporated and unincorporated Rpn11, we monitored the ubiquitin-AMC hydrolysis activity of 250 nM lid and Rpn11/Rpn8 MPN-domain dimers in reconstitution buffer containing the ATP regeneration system but with core particle, base, and Rpn10 omitted.
    </p>
   </sec>
   <sec id="s3-4">
    <title>
     Electron microscopy sample preparation
    </title>
    <p>
     For negative stain analysis, purified lid samples were diluted to ~50 nM in FLAG buffer (50 mM HEPES, pH7.6, 100 mM NaCl, 100 mM KCl) and directly applied to plasma-activated (20 s; 95% Ar, 5% O
     <sub>
      2
     </sub>
     ) copper grids for staining with 2% uranyl formate. For analysis by cryoEM, samples were diluted to ~5 uM in FLAG buffer that contained 1.5 mM TCEP (G Biosciences) and 0.05% NP-40 (Sigma). 4 μl of each sample was then applied directly to holey carbon C-flat grids (Protochips, 400 mesh, 1.2 μm holes) that had been plasma-cleaned (Gatan Solarus, 6 s; 95% Ar, 5% O
     <sub>
      2
     </sub>
     ) for manual blotting and plunge-freezing in liquid ethane.
    </p>
   </sec>
   <sec id="s3-5">
    <title>
     Electron microscopy
    </title>
    <p>
     All imaging data was collected using automated Leginon imaging software (
     <xref ref-type="bibr" rid="bib34">
      Suloway et al., 2005
     </xref>
     ). Images of negatively stained samples of wild-type and mutant lid complexes were acquired on a Tecnai Spirit LaB
     <sub>
      6
     </sub>
     electron microscope operating at 120 keV, with a random defocus range of -0.5 μm to -1.5 μm and an electron dose of 20 e
     <sup>
      -
     </sup>
     /Å
     <sup>
      2
     </sup>
     . 331 images were acquired for wild-type lid, 433 images for the Rpn5 (H282A/K283A) double-mutant, 412 images for the Rpn8 (K86A/K88A) double mutant, 181 for the Rpn5 (N275A) mutant, and 204 for the Rpn5 (Y273A) mutant. Images were collected at a nominal magnification of 52,000 X on an F416 CMOS 4K X 4K camera (TVIPS) with a pixel size of 2.05 Å/pixel at the sample level.
    </p>
    <p>
     Imaging of frozen hydrated samples was performed using a Titan Krios electron microscope operating at 300 keV, with a defocus range of -1.5 μm to -3.5 μm. A Gatan K2 Summit was used for counting individual electron events at a dose rate of 9.9e
     <sup>
      -
     </sup>
     /pixel/s, using an exposure of 7.6 s consisting of 38 frames at 200 ms/frame. This resulted in a total electron dose of 43.8 e
     <sup>
      -
     </sup>
     /Å
     <sup>
      2
     </sup>
     , accounting for coincidence loss. A total of 3,432 images of wild-type lid were acquired at a nominal magnification of 22,500X, yielding a pixel size of 0.655 Å/pixel at the sample level when collected in super-resolution mode.
    </p>
   </sec>
   <sec id="s3-6">
    <title>
     Negative stain image processing
    </title>
    <p>
     All image preprocessing was performed using the Appion image-processing pipeline (
     <xref ref-type="bibr" rid="bib22">
      Lander et al., 2009
     </xref>
     ). The contrast transfer function (CTF) was estimated using CTFFIND3 (
     <xref ref-type="bibr" rid="bib26">
      Mindell and Grigorieff, 2003
     </xref>
     ). For negative stain data, particles were selected using a difference of gaussians (DoG) picking algorithm (
     <xref ref-type="bibr" rid="bib39">
      Voss et al., 2009
     </xref>
     ), and only micrographs having an overall CTF confidence of greater than 80% were used for subsequent processing. The phases of the micrograph images were corrected according to the estimated CTF, and the particles were extracted using a box size of 160 pixels, and pixel values were capped at 4.5 sigma above or below the mean. Boxed particles were binned by a factor of 2 for processing. Reference-free 2D class averages of the extracted particles were determined through five rounds of iterative multivariate statistical analysis and multi-reference alignment (
     <xref ref-type="bibr" rid="bib27">
      Ogura et al., 2003
     </xref>
     ). The results of the 2D analysis were used to remove damaged, aggregated, or falsely selected particles from the dataset used for 3D analysis.
    </p>
    <p>
     All 3D analysis was performed with RELION v1.31 (
     <xref ref-type="bibr" rid="bib32">
      Scheres, 2012
     </xref>
     ). Using a previously determined reconstruction of the wild type yeast proteasome lid as an initial model (EMD-1993) (
     <xref ref-type="bibr" rid="bib21">
      Lander et al., 2012
     </xref>
     ), a 3D refinement of 17,680 particles wild-type lid complex provided a reconstruction at 19.6 Å resolution, according to a Fourier Shell Correlation at 0.143 of two independently determined half-maps. This volume was used as the initial model for all 3D analysis of the mutant lid datasets. 3D classification was performed on each of the negative stain mutant lid datasets, and only 3D classes exhibiting well-ordered structural details were selected and combined within each dataset for 3D refinement. 22,103 particles of the Rpn5 (H282A/K283A) mutant yielded a 25.2 Å reconstruction; 11,185 particles of the Rpn8 (K86A/K88A) mutant yielded a 27.3 Å reconstruction; 25,429 particles of the Rpn5 (N275A) mutant yielded a 23.4 Å reconstruction, and 44,272 particles of the Rpn5 (Y273A) mutant yielded a 21.8 Å reconstruction (
     <xref ref-type="fig" rid="fig2s2">
      Figure 2—figure supplement 2
     </xref>
     ). UCSF Chimera (
     <xref ref-type="bibr" rid="bib15">
      Goddard et al., 2007
     </xref>
     ) was used to dock the atomic model model of the lid into the density.
    </p>
   </sec>
   <sec id="s3-7">
    <title>
     Cryo-EM image processing
    </title>
    <p>
     For cryo-EM image preprocessing, the super-resolution images were binned by a factor of two in reciprocal space, and motion-corrected using MotionCorr (
     <xref ref-type="bibr" rid="bib23">
      Li et al., 2013
     </xref>
     ). The aligned frames were summed and used for all subsequent processing steps. The CTF was estimated using CTFFIND3 (
     <xref ref-type="bibr" rid="bib26">
      Mindell and Grigorieff, 2003
     </xref>
     ), and only micrographs having a CTF confidence value that was greater than 50% at 4Å resolution were used for further processing (
     <xref ref-type="fig" rid="fig1s1">
      Figure 1—figure supplement 1C
     </xref>
     ), resulting in a dataset of 3,365 micrographs. Particles were manually selected from the first 100 images, and the results of reference-free 2D analysis were used as templates for particle selection using FindEM (
     <xref ref-type="bibr" rid="bib29">
      Roseman, 2004
     </xref>
     ). A random subset of 50,000 particles were extracted from the micrographs with a box size of 256 and used for reference-free 2D analysis in order to rapidly assess the quality of particle selection (
     <xref ref-type="fig" rid="fig1s1">
      Figure 1—figure supplement 1B
     </xref>
     ). Very few classes corresponding to damaged or aggregated particles were observed; so all particles were used for single particle analysis in RELION.
    </p>
    <p>
     A total of 254,112 particles were extracted from the micrographs using a box size of 288 pixels, binned by a factor of 4, and classified into 8 3D classes over the course of 22 iterations in RELION. The particles from the 4 classes that showed evidence of conformational and compositional stability were selected from this initial classification, providing a total of 139,561 particles. The x and y coordinates corresponding to these particles were adjusted according to the final translational alignments from the 3D classification, and the centered particle coordinates were used to extract an unbinned particle dataset for 3D refinement in RELION.
    </p>
    <p>
     3D refinement using the default RELION parameters yielded a 4.4 Å resolution structure after 22 iterations. These aligned particle parameters were used for the RELION ‘particle polishing’ method. Individual particle motion trajectories were estimated using a running average window of 7 frames and particle translations were limited using a prior with a standard deviation of 1. Particle movements were fit to a linear trajectory using a running average window of 7 frames, with an inter-particle distance contribution value set to 300 pixels. Per-frame B-factors and intercepts were estimated by comparing the reconstructed half-maps from individual frames to the full-frame half maps, and the spatial frequency contribution from each frame weighted according (
     <xref ref-type="fig" rid="fig1s1">
      Figure 1—figure supplement 1D, E
     </xref>
     ). A new stack of particles was generated from the translationally aligned particles extracted from the weighted frames, which provided a reconstruction at 4.1 Å resolution.
    </p>
    <p>
     Due to the possibility that the flexible N-terminal domains of the PCI subunits were negatively influencing the particle alignment, a soft-edged 3D mask encompassing the PCI-domains, the helical bundle, and the MPN domains was generated (blue mask shown in
     <xref ref-type="fig" rid="fig1s2">
      Figure 1—figure supplement 2
     </xref>
     ) and used for 3D classification of the particles into 3 classes. This 3D classification was performed using the alignments from the 3D refinement, without further alignment of particles. One of the 3D classes resulting from this analysis clearly exhibited higher resolution details than the other two, and the 109,396 particles contained in this class were further refined (in the absence of a mask) to achieve a 3.6 Å structure. The same soft-edged 3D mask that was used for the previous 3D classification was then used for continued 3D refinement, which improved the structural details of the region contained within this mask, and increased the resolution to 3.5 Å resolution.
    </p>
   </sec>
   <sec id="s3-8">
    <title>
     Modeling
    </title>
    <p>
     Modeling and visualization of the lid was performed in COOT (
     <xref ref-type="bibr" rid="bib9">
      Emsley and Cowtan, 2004
     </xref>
     ) using mostly the cryo-EM map that had been generated using a soft mask encompassing the PCI domains and the C-terminal helical bundle (deposited as EMD-6479), as this is the highest resolved region, and cross-validated using the unmasked map. Available structures and homology models generated using Modeller v9.15 (
     <xref ref-type="bibr" rid="bib11">
      Eswar et al., 2007
     </xref>
     ) were initially fit into the unmasked cryo-EM map using Chimera (
     <xref ref-type="bibr" rid="bib15">
      Goddard et al., 2007
     </xref>
     ). These included: 1) the crystal structure of
     <italic>
      Drosophila melanogaster
     </italic>
     Rpn6 (residues 50–390) homolog (PDB ID: 3TXN) (
     <xref ref-type="bibr" rid="bib28">
      Pathare et al., 2014
     </xref>
     ); 2) the crystal structure of the
     <italic>
      Saccharomyces cerevisiae
     </italic>
     Rpn11-Rpn8 heterodimer (residues 24–220 and 10–280, respectively; PDB ID: 4O8X) (
     <xref ref-type="bibr" rid="bib40">
      Worden et al., 2014
     </xref>
     ); 3) the NMR structures of the N-terminal (residues 4–140 (PDB ID: 2MQW) and C-terminal (residues 184–353 (PDB ID: 2MRI)) domains of
     <italic>
      Saccharomyces cerevisiae
     </italic>
     Rpn9 (
     <xref ref-type="bibr" rid="bib19">
      Hu et al., 2015
     </xref>
     ); and 4) the N-terminal domain of
     <italic>
      Schizosaccharomyces pombe
     </italic>
     Rpn12 homolog (residues 6–200, PDB ID: 4B0Z) (
     <xref ref-type="bibr" rid="bib4">
      Boehringer et al., 2012
     </xref>
     ). The most N-terminal helices of Rpn5 and Rpn6 were not modeled due to the limited resolution of these regions. Placement of the N-terminal helices of Rpn3 was possible, however the absolute sequence register could not be assigned and these helices were modeled as polyalanine.
    </p>
    <p>
     Following each round of real space refinement in Phenix v1.10 (
     <xref ref-type="bibr" rid="bib1">
      Adams et al., 2010
     </xref>
     ), 100 models were generated in Rosetta (
     <xref ref-type="bibr" rid="bib8">
      DiMaio et al., 2015
     </xref>
     ), clustered, and scored. The top scoring structures were then used for the next round of manual model building and an aggregate model was used for refinement in Phenix. For the final round of refinement, the SHAKE protocol in Phenix was used to displace all atoms of the top 5 scoring models by 0.5 Å before refinement against one of the unmasked half-maps. An ensemble of these 5 models have been deposited in the PDB under ID: 3JCK.
    </p>
   </sec>
   <sec id="s3-9">
    <title>
     Visualizing rearrangements involved in lid incorporation to the 26S
    </title>
    <p>
     To visualize conformational changes undergone by the lid complex upon incorporation into the 26S proteasome, we first rigid-body fit individual components of the atomic model of our isolated lid (6 PCI domains, 6 N-terminal extensions, the MPN heterodimer, and the helical bundle) onto the pseudo-atomic model of the engaged lid (PDB-ID: 4CR2) (
     <xref ref-type="bibr" rid="bib37">
      Unverdorben et al., 2014
     </xref>
     ) using the ‘MatchMaker’ tool in Chimera. These overlaid models were then docked into the EM density of the 26S holoenzyme in the S1 state (
     <xref ref-type="bibr" rid="bib37">
      Unverdorben et al., 2014
     </xref>
     ). Overall, the secondary structure organization of the atomic models matched with high fidelity, although the register of the C-terminal helices of Rpn11 and the N-terminal helices of Rpn9 of the incorporated lid model were modified to correspond to the isolated lid model. The domain movements were visualized using the ‘morph conformations’ tool in UCSF Chimera. The motion of Rpn6 was evaluated using the software DynDom (
     <xref ref-type="bibr" rid="bib17">
      Hayward and Berendsen, 1998
     </xref>
     ).
    </p>
   </sec>
   <sec id="s3-10">
    <title>
     Accession codes
    </title>
    <p>
     The EM density maps for the 26S proteasome lid sub-complex before and after masked refinement, as well as unsharpened maps and half-maps, have been deposited in the Electron Microscopy Data Bank under accession number EMD-6479. The atomic coordinates of the five highest-scoring Rosetta models have been deposited under accession ID: 3JCK in the PDB.
    </p>
   </sec>
  </sec>
 </body>
 <back>
  <ack id="ack">
   <title>
    Acknowledgements
   </title>
   <p>
    We thank the members of the Lander and Martin labs for helpful discussions, and particularly Saikat Chowdhury and Lyn’Al Nosaka from GCL’s lab for their help with EM data collection and processing. We are also grateful to Jean-Christophe Ducom at TSRI HPC for establishing the necessary computational infrastructure to process the EM data. This research was funded in part by the Damon Runyon Cancer Research Foundation (DFS-#07-13), the Pew Scholars program, the Searle Scholars program, and the US National Institutes of Health (grant DP2 EB020402-01) to GCL. AM acknowledges support from the Searle Scholars Program, the US National Institutes of Health (grant R01-GM094497), the US National Science Foundation CAREER Program (NSF-MCB-1150288), and the Howard Hughes Medical Institute. EJW acknowledges support from the US National Science Foundation Graduate Research Fellowship.
   </p>
  </ack>
  <sec id="s4" sec-type="additional-information">
   <title>
    Additional information
   </title>
   <fn-group content-type="competing-interest">
    <title>
     Competing interests
    </title>
    <fn fn-type="conflict" id="conf1">
     <p>
      The authors declare that no competing interests exist.
     </p>
    </fn>
   </fn-group>
   <fn-group content-type="author-contribution">
    <title>
     Author contributions
    </title>
    <fn fn-type="con" id="con1">
     <p>
      CMD, Performed the EM data collection and processing, Conception and design, Acquisition of data, Analysis and interpretation of data, Drafting or revising the article
     </p>
    </fn>
    <fn fn-type="con" id="con2">
     <p>
      EJW, Expressed and purified wild type and mutant proteasome components for EM analysis, and performed biochemical experiments, Conception and design, Acquisition of data, Analysis and interpretation of data, Drafting or revising the article
     </p>
    </fn>
    <fn fn-type="con" id="con3">
     <p>
      MAH, Performed the atomic modeling, Analysis and interpretation of data, Drafting or revising the article
     </p>
    </fn>
    <fn fn-type="con" id="con4">
     <p>
      AM, Conception and design, Acquisition of data, Analysis and interpretation of data, Drafting or revising the article
     </p>
    </fn>
    <fn fn-type="con" id="con5">
     <p>
      GCL, Performed the EM data collection and processing, Conception and design, Acquisition of data, Analysis and interpretation of data, Drafting or revising the article
     </p>
    </fn>
   </fn-group>
  </sec>
  <sec id="s5" sec-type="supplementary-material">
   <title>
    Additional files
   </title>
   <sec id="s6" sec-type="datasets">
    <title>
     Major datasets
    </title>
    <p>
     The following datasets were generated:
    </p>
    <p>
     <related-object content-type="generated-dataset" id="dataro1" source-id="http://www.rcsb.org/pdb/explore/explore.do?structureId=3JCK" source-id-type="uri">
      <collab>
       Herzik Jr MA
      </collab>
      ,
      <collab>
       Dambacher CM
      </collab>
      ,
      <collab>
       Worden EJ
      </collab>
      ,
      <collab>
       Martin A
      </collab>
      ,
      <collab>
       Lander GC
      </collab>
      <x>
       ,
      </x>
      <year>
       2016
      </year>
      <x>
       ,
      </x>
      <source>
       Structure of the yeast 26S proteasome lid sub-complex
      </source>
      <x>
       ,
      </x>
      <ext-link ext-link-type="uri" xlink:href="http://www.rcsb.org/pdb/explore/explore.do?structureId=3JCK">
       http://www.rcsb.org/pdb/explore/explore.do?structureId=3JCK
      </ext-link>
      <x>
       ,
      </x>
      <comment>
       Publicly available at the RSCB Protein Data Bank (accession no. 3JCK)
      </comment>
     </related-object>
    </p>
   </sec>
  </sec>
  <ref-list>
   <title>
    References
   </title>
   <ref id="bib1">
    <element-citation publication-type="journal">
     <person-group person-group-type="author">
      <name>
       <surname>
        Adams
       </surname>
       <given-names>
        PD
       </given-names>
      </name>
      <name>
       <surname>
        Afonine
       </surname>
       <given-names>
        PV
       </given-names>
      </name>
      <name>
       <surname>
        Bunkóczi
       </surname>
       <given-names>
        G
       </given-names>
      </name>
      <name>
       <surname>
        Chen
       </surname>
       <given-names>
        VB
       </given-names>
      </name>
      <name>
       <surname>
        Davis
       </surname>
       <given-names>
        IW
       </given-names>
      </name>
      <name>
       <surname>
        Echols
       </surname>
       <given-names>
        N
       </given-names>
      </name>
      <name>
       <surname>
        Headd
       </surname>
       <given-names>
        JJ
       </given-names>
      </name>
      <name>
       <surname>
        Hung
       </surname>
       <given-names>
        L-W
       </given-names>
      </name>
      <name>
       <surname>
        Kapral
       </surname>
       <given-names>
        GJ
       </given-names>
      </name>
      <name>
       <surname>
        Grosse-Kunstleve
       </surname>
       <given-names>
        RW
       </given-names>
      </name>
      <name>
       <surname>
        McCoy
       </surname>
       <given-names>
        AJ
       </given-names>
      </name>
      <name>
       <surname>
        Moriarty
       </surname>
       <given-names>
        NW
       </given-names>
      </name>
      <name>
       <surname>
        Oeffner
       </surname>
       <given-names>
        R
       </given-names>
      </name>
      <name>
       <surname>
        Read
       </surname>
       <given-names>
        RJ
       </given-names>
      </name>
      <name>
       <surname>
        Richardson
       </surname>
       <given-names>
        DC
       </given-names>
      </name>
      <name>
       <surname>
        Richardson
       </surname>
       <given-names>
        JS
       </given-names>
      </name>
      <name>
       <surname>
        Terwilliger
       </surname>
       <given-names>
        TC
       </given-names>
      </name>
      <name>
       <surname>
        Zwart
       </surname>
       <given-names>
        PH
       </given-names>
      </name>
     </person-group>
     <year iso-8601-date="2010">
      2010
     </year>
     <article-title>
      <italic>
       PHENIX
      </italic>
      : a comprehensive python-based system for macromolecular structure solution
     </article-title>
     <source>
      Acta Crystallographica Section D Biological Crystallography
     </source>
     <volume>
      66
     </volume>
     <fpage>
      213
     </fpage>
     <lpage>
      221
     </lpage>
     <pub-id pub-id-type="doi">
      10.1107/S0907444909052925
     </pub-id>
    </element-citation>
   </ref>
   <ref id="bib2">
    <element-citation publication-type="journal">
     <person-group person-group-type="author">
      <name>
       <surname>
        Beck
       </surname>
       <given-names>
        F
       </given-names>
      </name>
      <name>
       <surname>
        Unverdorben
       </surname>
       <given-names>
        P
       </given-names>
      </name>
      <name>
       <surname>
        Bohn
       </surname>
       <given-names>
        S
       </given-names>
      </name>
      <name>
       <surname>
        Schweitzer
       </surname>
       <given-names>
        A
       </given-names>
      </name>
      <name>
       <surname>
        Pfeifer
       </surname>
       <given-names>
        G
       </given-names>
      </name>
      <name>
       <surname>
        Sakata
       </surname>
       <given-names>
        E
       </given-names>
      </name>
      <name>
       <surname>
        Nickell
       </surname>
       <given-names>
        S
       </given-names>
      </name>
      <name>
       <surname>
        Plitzko
       </surname>
       <given-names>
        JM
       </given-names>
      </name>
      <name>
       <surname>
        Villa
       </surname>
       <given-names>
        E
       </given-names>
      </name>
      <name>
       <surname>
        Baumeister
       </surname>
       <given-names>
        W
       </given-names>
      </name>
      <name>
       <surname>
        Forster
       </surname>
       <given-names>
        F
       </given-names>
      </name>
     </person-group>
     <year iso-8601-date="2012">
      2012
     </year>
     <article-title>
      Near-atomic resolution structural model of the yeast 26S proteasome
     </article-title>
     <source>
      Proceedings of the National Academy of Sciences of the United States of America
     </source>
     <volume>
      109
     </volume>
     <fpage>
      14870
     </fpage>
     <lpage>
      14875
     </lpage>
     <pub-id pub-id-type="doi">
      10.1073/pnas.1213333109
     </pub-id>
    </element-citation>
   </ref>
   <ref id="bib3">
    <element-citation publication-type="journal">
     <person-group person-group-type="author">
      <name>
       <surname>
        Beckwith
       </surname>
       <given-names>
        R
       </given-names>
      </name>
      <name>
       <surname>
        Estrin
       </surname>
       <given-names>
        E
       </given-names>
      </name>
      <name>
       <surname>
        Worden
       </surname>
       <given-names>
        EJ
       </given-names>
      </name>
      <name>
       <surname>
        Martin
       </surname>
       <given-names>
        A
       </given-names>
      </name>
     </person-group>
     <year iso-8601-date="2013">
      2013
     </year>
     <article-title>
      Reconstitution of the 26S proteasome reveals functional asymmetries in its AAA+ unfoldase
     </article-title>
     <source>
      Nature Structural &amp; Molecular Biology
     </source>
     <volume>
      20
     </volume>
     <fpage>
      1164
     </fpage>
     <lpage>
      1172
     </lpage>
     <pub-id pub-id-type="doi">
      10.1038/nsmb.2659
     </pub-id>
    </element-citation>
   </ref>
   <ref id="bib4">
    <element-citation publication-type="journal">
     <person-group person-group-type="author">
      <name>
       <surname>
        Boehringer
       </surname>
       <given-names>
        J
       </given-names>
      </name>
      <name>
       <surname>
        Riedinger
       </surname>
       <given-names>
        C
       </given-names>
      </name>
      <name>
       <surname>
        Paraskevopoulos
       </surname>
       <given-names>
        K
       </given-names>
      </name>
      <name>
       <surname>
        Johnson
       </surname>
       <given-names>
        EOD
       </given-names>
      </name>
      <name>
       <surname>
        Lowe
       </surname>
       <given-names>
        ED
       </given-names>
      </name>
      <name>
       <surname>
        Khoudian
       </surname>
       <given-names>
        C
       </given-names>
      </name>
      <name>
       <surname>
        Smith
       </surname>
       <given-names>
        D
       </given-names>
      </name>
      <name>
       <surname>
        Noble
       </surname>
       <given-names>
        MEM
       </given-names>
      </name>
      <name>
       <surname>
        Gordon
       </surname>
       <given-names>
        C
       </given-names>
      </name>
      <name>
       <surname>
        Endicott
       </surname>
       <given-names>
        JA
       </given-names>
      </name>
     </person-group>
     <year iso-8601-date="2012">
      2012
     </year>
     <article-title>
      Structural and functional characterization of Rpn12 identifies residues required for Rpn10 proteasome incorporation
     </article-title>
     <source>
      Biochemical Journal
     </source>
     <volume>
      448
     </volume>
     <fpage>
      55
     </fpage>
     <lpage>
      65
     </lpage>
     <pub-id pub-id-type="doi">
      10.1042/BJ20120542
     </pub-id>
    </element-citation>
   </ref>
   <ref id="bib5">
    <element-citation publication-type="journal">
     <person-group person-group-type="author">
      <name>
       <surname>
        Bohn
       </surname>
       <given-names>
        S
       </given-names>
      </name>
      <name>
       <surname>
        Sakata
       </surname>
       <given-names>
        E
       </given-names>
      </name>
      <name>
       <surname>
        Beck
       </surname>
       <given-names>
        F
       </given-names>
      </name>
      <name>
       <surname>
        Pathare
       </surname>
       <given-names>
        GR
       </given-names>
      </name>
      <name>
       <surname>
        Schnitger
       </surname>
       <given-names>
        J
       </given-names>
      </name>
      <name>
       <surname>
        Nágy
       </surname>
       <given-names>
        I
       </given-names>
      </name>
      <name>
       <surname>
        Baumeister
       </surname>
       <given-names>
        W
       </given-names>
      </name>
      <name>
       <surname>
        Förster
       </surname>
       <given-names>
        F
       </given-names>
      </name>
     </person-group>
     <year iso-8601-date="2013">
      2013
     </year>
     <article-title>
      Localization of the regulatory particle subunit Sem1 in the 26S proteasome
     </article-title>
     <source>
      Biochemical and Biophysical Research Communications
     </source>
     <volume>
      435
     </volume>
     <fpage>
      250
     </fpage>
     <lpage>
      254
     </lpage>
     <pub-id pub-id-type="doi">
      10.1016/j.bbrc.2013.04.069
     </pub-id>
    </element-citation>
   </ref>
   <ref id="bib6">
    <element-citation publication-type="journal">
     <person-group person-group-type="author">
      <name>
       <surname>
        Davies
       </surname>
       <given-names>
        CW
       </given-names>
      </name>
      <name>
       <surname>
        Paul
       </surname>
       <given-names>
        LN
       </given-names>
      </name>
      <name>
       <surname>
        Kim
       </surname>
       <given-names>
        M-I
       </given-names>
      </name>
      <name>
       <surname>
        Das
       </surname>
       <given-names>
        C
       </given-names>
      </name>
     </person-group>
     <year iso-8601-date="2011">
      2011
     </year>
     <article-title>
      Structural and thermodynamic comparison of the catalytic domain of AMSH and AMSH-LP: nearly identical fold but different stability
     </article-title>
     <source>
      Journal of Molecular Biology
     </source>
     <volume>
      413
     </volume>
     <fpage>
      416
     </fpage>
     <lpage>
      429
     </lpage>
     <pub-id pub-id-type="doi">
      10.1016/j.jmb.2011.08.029
     </pub-id>
    </element-citation>
   </ref>
   <ref id="bib7">
    <element-citation publication-type="journal">
     <person-group person-group-type="author">
      <name>
       <surname>
        des Georges
       </surname>
       <given-names>
        A
       </given-names>
      </name>
      <name>
       <surname>
        Dhote
       </surname>
       <given-names>
        V
       </given-names>
      </name>
      <name>
       <surname>
        Kuhn
       </surname>
       <given-names>
        L
       </given-names>
      </name>
      <name>
       <surname>
        Hellen
       </surname>
       <given-names>
        CUT
       </given-names>
      </name>
      <name>
       <surname>
        Pestova
       </surname>
       <given-names>
        TV
       </given-names>
      </name>
      <name>
       <surname>
        Frank
       </surname>
       <given-names>
        J
       </given-names>
      </name>
      <name>
       <surname>
        Hashem
       </surname>
       <given-names>
        Y
       </given-names>
      </name>
     </person-group>
     <year iso-8601-date="2015">
      2015
     </year>
     <article-title>
      Structure of mammalian eIF3 in the context of the 43S preinitiation complex
     </article-title>
     <source>
      Nature
     </source>
     <volume>
      525
     </volume>
     <fpage>
      491
     </fpage>
     <lpage>
      495
     </lpage>
     <pub-id pub-id-type="doi">
      10.1038/nature14891
     </pub-id>
    </element-citation>
   </ref>
   <ref id="bib8">
    <element-citation publication-type="journal">
     <person-group person-group-type="author">
      <name>
       <surname>
        DiMaio
       </surname>
       <given-names>
        F
       </given-names>
      </name>
      <name>
       <surname>
        Song
       </surname>
       <given-names>
        Y
       </given-names>
      </name>
      <name>
       <surname>
        Li
       </surname>
       <given-names>
        X
       </given-names>
      </name>
      <name>
       <surname>
        Brunner
       </surname>
       <given-names>
        MJ
       </given-names>
      </name>
      <name>
       <surname>
        Xu
       </surname>
       <given-names>
        C
       </given-names>
      </name>
      <name>
       <surname>
        Conticello
       </surname>
       <given-names>
        V
       </given-names>
      </name>
      <name>
       <surname>
        Egelman
       </surname>
       <given-names>
        E
       </given-names>
      </name>
      <name>
       <surname>
        Marlovits
       </surname>
       <given-names>
        TC
       </given-names>
      </name>
      <name>
       <surname>
        Cheng
       </surname>
       <given-names>
        Y
       </given-names>
      </name>
      <name>
       <surname>
        Baker
       </surname>
       <given-names>
        D
       </given-names>
      </name>
     </person-group>
     <year iso-8601-date="2015">
      2015
     </year>
     <article-title>
      Atomic-accuracy models from 4.5-å cryo-electron microscopy data with density-guided iterative local refinement
     </article-title>
     <source>
      Nature Methods
     </source>
     <volume>
      12
     </volume>
     <fpage>
      361
     </fpage>
     <lpage>
      365
     </lpage>
     <pub-id pub-id-type="doi">
      10.1038/nmeth.3286
     </pub-id>
    </element-citation>
   </ref>
   <ref id="bib9">
    <element-citation publication-type="journal">
     <person-group person-group-type="author">
      <name>
       <surname>
        Emsley
       </surname>
       <given-names>
        P
       </given-names>
      </name>
      <name>
       <surname>
        Cowtan
       </surname>
       <given-names>
        K
       </given-names>
      </name>
     </person-group>
     <year iso-8601-date="2004">
      2004
     </year>
     <article-title>
      <italic>
       Coot
      </italic>
      : model-building tools for molecular graphics
     </article-title>
     <source>
      Acta Crystallographica Section D Biological Crystallography
     </source>
     <volume>
      60
     </volume>
     <fpage>
      2126
     </fpage>
     <lpage>
      2132
     </lpage>
     <pub-id pub-id-type="doi">
      10.1107/S0907444904019158
     </pub-id>
    </element-citation>
   </ref>
   <ref id="bib10">
    <element-citation publication-type="journal">
     <person-group person-group-type="author">
      <name>
       <surname>
        Estrin
       </surname>
       <given-names>
        E
       </given-names>
      </name>
      <name>
       <surname>
        Lopez-Blanco
       </surname>
       <given-names>
        JR
       </given-names>
      </name>
      <name>
       <surname>
        Chacón
       </surname>
       <given-names>
        P
       </given-names>
      </name>
      <name>
       <surname>
        Martin
       </surname>
       <given-names>
        A
       </given-names>
      </name>
     </person-group>
     <year iso-8601-date="2013">
      2013
     </year>
     <article-title>
      Formation of an intricate helical bundle dictates the assembly of the 26S proteasome lid
     </article-title>
     <source>
      Structure
     </source>
     <volume>
      21
     </volume>
     <fpage>
      1624
     </fpage>
     <lpage>
      1635
     </lpage>
     <pub-id pub-id-type="doi">
      10.1016/j.str.2013.06.023
     </pub-id>
    </element-citation>
   </ref>
   <ref id="bib11">
    <element-citation publication-type="journal">
     <person-group person-group-type="author">
      <name>
       <surname>
        Eswar
       </surname>
       <given-names>
        N
       </given-names>
      </name>
      <name>
       <surname>
        Webb
       </surname>
       <given-names>
        B
       </given-names>
      </name>
      <name>
       <surname>
        Marti-Renom
       </surname>
       <given-names>
        MA
       </given-names>
      </name>
      <name>
       <surname>
        Madhusudhan
       </surname>
       <given-names>
        MS
       </given-names>
      </name>
      <name>
       <surname>
        Eramian
       </surname>
       <given-names>
        D
       </given-names>
      </name>
      <name>
       <surname>
        Shen
       </surname>
       <given-names>
        Min-yi
       </given-names>
      </name>
      <name>
       <surname>
        Pieper
       </surname>
       <given-names>
        U
       </given-names>
      </name>
      <name>
       <surname>
        Sali
       </surname>
       <given-names>
        A
       </given-names>
      </name>
     </person-group>
     <year iso-8601-date="2007">
      2007
     </year>
     <article-title>
      Comparative protein structure modeling using MODELLER
     </article-title>
     <source>
      Current Protocols in Protein Science
     </source>
     <volume>
      2
     </volume>
     <pub-id pub-id-type="doi">
      10.1002/0471140864.ps0209s50
     </pub-id>
    </element-citation>
   </ref>
   <ref id="bib12">
    <element-citation publication-type="journal">
     <person-group person-group-type="author">
      <name>
       <surname>
        Finley
       </surname>
       <given-names>
        D
       </given-names>
      </name>
     </person-group>
     <year iso-8601-date="2009">
      2009
     </year>
     <article-title>
      Recognition and processing of ubiquitin-protein conjugates by the proteasome
     </article-title>
     <source>
      Annual Review of Biochemistry
     </source>
     <volume>
      78
     </volume>
     <fpage>
      477
     </fpage>
     <lpage>
      513
     </lpage>
     <pub-id pub-id-type="doi">
      10.1146/annurev.biochem.78.081507.101607
     </pub-id>
    </element-citation>
   </ref>
   <ref id="bib13">
    <element-citation publication-type="journal">
     <person-group person-group-type="author">
      <name>
       <surname>
        Gerke
       </surname>
       <given-names>
        V
       </given-names>
      </name>
      <name>
       <surname>
        Moss
       </surname>
       <given-names>
        SE
       </given-names>
      </name>
     </person-group>
     <year iso-8601-date="2002">
      2002
     </year>
     <article-title>
      Annexins: from structure to function
     </article-title>
     <source>
      Physiological Reviews
     </source>
     <volume>
      82
     </volume>
     <fpage>
      331
     </fpage>
     <lpage>
      371
     </lpage>
     <pub-id pub-id-type="doi">
      10.1152/physrev.00030.2001
     </pub-id>
    </element-citation>
   </ref>
   <ref id="bib14">
    <element-citation publication-type="journal">
     <person-group person-group-type="author">
      <name>
       <surname>
        Glickman
       </surname>
       <given-names>
        MH
       </given-names>
      </name>
      <name>
       <surname>
        Rubin
       </surname>
       <given-names>
        DM
       </given-names>
      </name>
      <name>
       <surname>
        Coux
       </surname>
       <given-names>
        O
       </given-names>
      </name>
      <name>
       <surname>
        Wefes
       </surname>
       <given-names>
        I
       </given-names>
      </name>
      <name>
       <surname>
        Pfeifer
       </surname>
       <given-names>
        G
       </given-names>
      </name>
      <name>
       <surname>
        Cjeka
       </surname>
       <given-names>
        Z
       </given-names>
      </name>
      <name>
       <surname>
        Baumeister
       </surname>
       <given-names>
        W
       </given-names>
      </name>
      <name>
       <surname>
        Fried
       </surname>
       <given-names>
        VA
       </given-names>
      </name>
      <name>
       <surname>
        Finley
       </surname>
       <given-names>
        D
       </given-names>
      </name>
     </person-group>
     <year iso-8601-date="1998">
      1998
     </year>
     <article-title>
      A subcomplex of the proteasome regulatory particle required for ubiquitin-conjugate degradation and related to the COP9-signalosome and eIF3
     </article-title>
     <source>
      Cell
     </source>
     <volume>
      94
     </volume>
     <fpage>
      615
     </fpage>
     <lpage>
      623
     </lpage>
     <pub-id pub-id-type="doi">
      10.1016/S0092-8674(00)81603-7
     </pub-id>
    </element-citation>
   </ref>
   <ref id="bib15">
    <element-citation publication-type="journal">
     <person-group person-group-type="author">
      <name>
       <surname>
        Goddard
       </surname>
       <given-names>
        TD
       </given-names>
      </name>
      <name>
       <surname>
        Huang
       </surname>
       <given-names>
        CC
       </given-names>
      </name>
      <name>
       <surname>
        Ferrin
       </surname>
       <given-names>
        TE
       </given-names>
      </name>
     </person-group>
     <year iso-8601-date="2007">
      2007
     </year>
     <article-title>
      Visualizing density maps with UCSF chimera
     </article-title>
     <source>
      Journal of Structural Biology
     </source>
     <volume>
      157
     </volume>
     <fpage>
      281
     </fpage>
     <lpage>
      287
     </lpage>
     <pub-id pub-id-type="doi">
      10.1016/j.jsb.2006.06.010
     </pub-id>
    </element-citation>
   </ref>
   <ref id="bib16">
    <element-citation publication-type="journal">
     <person-group person-group-type="author">
      <name>
       <surname>
        Groll
       </surname>
       <given-names>
        M
       </given-names>
      </name>
      <name>
       <surname>
        Ditzel
       </surname>
       <given-names>
        L
       </given-names>
      </name>
      <name>
       <surname>
        Löwe
       </surname>
       <given-names>
        J
       </given-names>
      </name>
      <name>
       <surname>
        Stock
       </surname>
       <given-names>
        D
       </given-names>
      </name>
      <name>
       <surname>
        Bochtler
       </surname>
       <given-names>
        M
       </given-names>
      </name>
      <name>
       <surname>
        Bartunik
       </surname>
       <given-names>
        HD
       </given-names>
      </name>
      <name>
       <surname>
        Huber
       </surname>
       <given-names>
        R
       </given-names>
      </name>
     </person-group>
     <year iso-8601-date="1997">
      1997
     </year>
     <article-title>
      Structure of 20S proteasome from yeast at 2.4Å resolution
     </article-title>
     <source>
      Nature
     </source>
     <volume>
      386
     </volume>
     <fpage>
      463
     </fpage>
     <lpage>
      471
     </lpage>
     <pub-id pub-id-type="doi">
      10.1038/386463a0
     </pub-id>
    </element-citation>
   </ref>
   <ref id="bib17">
    <element-citation publication-type="journal">
     <person-group person-group-type="author">
      <name>
       <surname>
        Hayward
       </surname>
       <given-names>
        S
       </given-names>
      </name>
      <name>
       <surname>
        Berendsen
       </surname>
       <given-names>
        HJC
       </given-names>
      </name>
     </person-group>
     <year iso-8601-date="1998">
      1998
     </year>
     <article-title>
      Systematic analysis of domain motions in proteins from conformational change: new results on citrate synthase and T4 lysozyme
     </article-title>
     <source>
      Proteins
     </source>
     <volume>
      30
     </volume>
     <fpage>
      144
     </fpage>
     <lpage>
      154
     </lpage>
     <pub-id pub-id-type="doi">
      10.1002/(SICI)1097-0134(19980201)30:2&lt;144::AID-PROT4&gt;3.0.CO;2-N
     </pub-id>
    </element-citation>
   </ref>
   <ref id="bib18">
    <element-citation publication-type="journal">
     <person-group person-group-type="author">
      <name>
       <surname>
        Heymann
       </surname>
       <given-names>
        JB
       </given-names>
      </name>
      <name>
       <surname>
        Belnap
       </surname>
       <given-names>
        DM
       </given-names>
      </name>
     </person-group>
     <year iso-8601-date="2007">
      2007
     </year>
     <article-title>
      Bsoft: image processing and molecular modeling for electron microscopy
     </article-title>
     <source>
      Journal of Structural Biology
     </source>
     <volume>
      157
     </volume>
     <fpage>
      3
     </fpage>
     <lpage>
      18
     </lpage>
     <pub-id pub-id-type="doi">
      10.1016/j.jsb.2006.06.006
     </pub-id>
    </element-citation>
   </ref>
   <ref id="bib19">
    <element-citation publication-type="journal">
     <person-group person-group-type="author">
      <name>
       <surname>
        Hu
       </surname>
       <given-names>
        Y
       </given-names>
      </name>
      <name>
       <surname>
        Wu
       </surname>
       <given-names>
        Y
       </given-names>
      </name>
      <name>
       <surname>
        Li
       </surname>
       <given-names>
        Q
       </given-names>
      </name>
      <name>
       <surname>
        Zhang
       </surname>
       <given-names>
        W
       </given-names>
      </name>
      <name>
       <surname>
        Jin
       </surname>
       <given-names>
        C
       </given-names>
      </name>
     </person-group>
     <year iso-8601-date="2015">
      2015
     </year>
     <article-title>
      Solution structure of yeast Rpn9
     </article-title>
     <source>
      Journal of Biological Chemistry
     </source>
     <volume>
      290
     </volume>
     <fpage>
      6878
     </fpage>
     <lpage>
      6889
     </lpage>
     <pub-id pub-id-type="doi">
      10.1074/jbc.M114.626762
     </pub-id>
    </element-citation>
   </ref>
   <ref id="bib20">
    <element-citation publication-type="journal">
     <person-group person-group-type="author">
      <name>
       <surname>
        Komander
       </surname>
       <given-names>
        D
       </given-names>
      </name>
      <name>
       <surname>
        Clague
       </surname>
       <given-names>
        MJ
       </given-names>
      </name>
      <name>
       <surname>
        Urbé
       </surname>
       <given-names>
        S
       </given-names>
      </name>
     </person-group>
     <year iso-8601-date="2009">
      2009
     </year>
     <article-title>
      Breaking the chains: structure and function of the deubiquitinases
     </article-title>
     <source>
      Nature Reviews Molecular Cell Biology
     </source>
     <volume>
      10
     </volume>
     <fpage>
      550
     </fpage>
     <lpage>
      563
     </lpage>
     <pub-id pub-id-type="doi">
      10.1038/nrm2731
     </pub-id>
    </element-citation>
   </ref>
   <ref id="bib21">
    <element-citation publication-type="journal">
     <person-group person-group-type="author">
      <name>
       <surname>
        Lander
       </surname>
       <given-names>
        GC
       </given-names>
      </name>
      <name>
       <surname>
        Estrin
       </surname>
       <given-names>
        E
       </given-names>
      </name>
      <name>
       <surname>
        Matyskiela
       </surname>
       <given-names>
        ME
       </given-names>
      </name>
      <name>
       <surname>
        Bashore
       </surname>
       <given-names>
        C
       </given-names>
      </name>
      <name>
       <surname>
        Nogales
       </surname>
       <given-names>
        E
       </given-names>
      </name>
      <name>
       <surname>
        Martin
       </surname>
       <given-names>
        A
       </given-names>
      </name>
     </person-group>
     <year iso-8601-date="2012">
      2012
     </year>
     <article-title>
      Complete subunit architecture of the proteasome regulatory particle
     </article-title>
     <source>
      Nature
     </source>
     <volume>
      482
     </volume>
     <fpage>
      186
     </fpage>
     <lpage>
      191
     </lpage>
     <pub-id pub-id-type="doi">
      10.1038/nature10774
     </pub-id>
    </element-citation>
   </ref>
   <ref id="bib22">
    <element-citation publication-type="journal">
     <person-group person-group-type="author">
      <name>
       <surname>
        Lander
       </surname>
       <given-names>
        GC
       </given-names>
      </name>
      <name>
       <surname>
        Stagg
       </surname>
       <given-names>
        SM
       </given-names>
      </name>
      <name>
       <surname>
        Voss
       </surname>
       <given-names>
        NR
       </given-names>
      </name>
      <name>
       <surname>
        Cheng
       </surname>
       <given-names>
        A
       </given-names>
      </name>
      <name>
       <surname>
        Fellmann
       </surname>
       <given-names>
        D
       </given-names>
      </name>
      <name>
       <surname>
        Pulokas
       </surname>
       <given-names>
        J
       </given-names>
      </name>
      <name>
       <surname>
        Yoshioka
       </surname>
       <given-names>
        C
       </given-names>
      </name>
      <name>
       <surname>
        Irving
       </surname>
       <given-names>
        C
       </given-names>
      </name>
      <name>
       <surname>
        Mulder
       </surname>
       <given-names>
        A
       </given-names>
      </name>
      <name>
       <surname>
        Lau
       </surname>
       <given-names>
        P-W
       </given-names>
      </name>
      <name>
       <surname>
        Lyumkis
       </surname>
       <given-names>
        D
       </given-names>
      </name>
      <name>
       <surname>
        Potter
       </surname>
       <given-names>
        CS
       </given-names>
      </name>
      <name>
       <surname>
        Carragher
       </surname>
       <given-names>
        B
       </given-names>
      </name>
     </person-group>
     <year iso-8601-date="2009">
      2009
     </year>
     <article-title>
      Appion: an integrated, database-driven pipeline to facilitate EM image processing
     </article-title>
     <source>
      Journal of Structural Biology
     </source>
     <volume>
      166
     </volume>
     <fpage>
      95
     </fpage>
     <lpage>
      102
     </lpage>
     <pub-id pub-id-type="doi">
      10.1016/j.jsb.2009.01.002
     </pub-id>
    </element-citation>
   </ref>
   <ref id="bib23">
    <element-citation publication-type="journal">
     <person-group person-group-type="author">
      <name>
       <surname>
        Li
       </surname>
       <given-names>
        X
       </given-names>
      </name>
      <name>
       <surname>
        Mooney
       </surname>
       <given-names>
        P
       </given-names>
      </name>
      <name>
       <surname>
        Zheng
       </surname>
       <given-names>
        S
       </given-names>
      </name>
      <name>
       <surname>
        Booth
       </surname>
       <given-names>
        CR
       </given-names>
      </name>
      <name>
       <surname>
        Braunfeld
       </surname>
       <given-names>
        MB
       </given-names>
      </name>
      <name>
       <surname>
        Gubbens
       </surname>
       <given-names>
        S
       </given-names>
      </name>
      <name>
       <surname>
        Agard
       </surname>
       <given-names>
        DA
       </given-names>
      </name>
      <name>
       <surname>
        Cheng
       </surname>
       <given-names>
        Y
       </given-names>
      </name>
     </person-group>
     <year iso-8601-date="2013">
      2013
     </year>
     <article-title>
      Electron counting and beam-induced motion correction enable near-atomic-resolution single-particle cryo-EM
     </article-title>
     <source>
      Nature Methods
     </source>
     <volume>
      10
     </volume>
     <fpage>
      584
     </fpage>
     <lpage>
      590
     </lpage>
     <pub-id pub-id-type="doi">
      10.1038/nmeth.2472
     </pub-id>
    </element-citation>
   </ref>
   <ref id="bib24">
    <element-citation publication-type="journal">
     <person-group person-group-type="author">
      <name>
       <surname>
        Lingaraju
       </surname>
       <given-names>
        GM
       </given-names>
      </name>
      <name>
       <surname>
        Bunker
       </surname>
       <given-names>
        RD
       </given-names>
      </name>
      <name>
       <surname>
        Cavadini
       </surname>
       <given-names>
        S
       </given-names>
      </name>
      <name>
       <surname>
        Hess
       </surname>
       <given-names>
        D
       </given-names>
      </name>
      <name>
       <surname>
        Hassiepen
       </surname>
       <given-names>
        U
       </given-names>
      </name>
      <name>
       <surname>
        Renatus
       </surname>
       <given-names>
        M
       </given-names>
      </name>
      <name>
       <surname>
        Fischer
       </surname>
       <given-names>
        ES
       </given-names>
      </name>
      <name>
       <surname>
        Thomä
       </surname>
       <given-names>
        NH
       </given-names>
      </name>
     </person-group>
     <year iso-8601-date="2014">
      2014
     </year>
     <article-title>
      Crystal structure of the human COP9 signalosome
     </article-title>
     <source>
      Nature
     </source>
     <volume>
      512
     </volume>
     <fpage>
      161
     </fpage>
     <lpage>
      165
     </lpage>
     <pub-id pub-id-type="doi">
      10.1038/nature13566
     </pub-id>
    </element-citation>
   </ref>
   <ref id="bib25">
    <element-citation publication-type="journal">
     <person-group person-group-type="author">
      <name>
       <surname>
        Matyskiela
       </surname>
       <given-names>
        ME
       </given-names>
      </name>
      <name>
       <surname>
        Lander
       </surname>
       <given-names>
        GC
       </given-names>
      </name>
      <name>
       <surname>
        Martin
       </surname>
       <given-names>
        A
       </given-names>
      </name>
     </person-group>
     <year iso-8601-date="2013">
      2013
     </year>
     <article-title>
      Conformational switching of the 26S proteasome enables substrate degradation
     </article-title>
     <source>
      Nature Structural &amp; Molecular Biology
     </source>
     <volume>
      20
     </volume>
     <fpage>
      781
     </fpage>
     <lpage>
      788
     </lpage>
     <pub-id pub-id-type="doi">
      10.1038/nsmb.2616
     </pub-id>
    </element-citation>
   </ref>
   <ref id="bib26">
    <element-citation publication-type="journal">
     <person-group person-group-type="author">
      <name>
       <surname>
        Mindell
       </surname>
       <given-names>
        JA
       </given-names>
      </name>
      <name>
       <surname>
        Grigorieff
       </surname>
       <given-names>
        N
       </given-names>
      </name>
     </person-group>
     <year iso-8601-date="2003">
      2003
     </year>
     <article-title>
      Accurate determination of local defocus and specimen tilt in electron microscopy
     </article-title>
     <source>
      Journal of Structural Biology
     </source>
     <volume>
      142
     </volume>
     <fpage>
      334
     </fpage>
     <lpage>
      347
     </lpage>
     <pub-id pub-id-type="doi">
      10.1016/S1047-8477(03)00069-8
     </pub-id>
    </element-citation>
   </ref>
   <ref id="bib27">
    <element-citation publication-type="journal">
     <person-group person-group-type="author">
      <name>
       <surname>
        Ogura
       </surname>
       <given-names>
        T
       </given-names>
      </name>
      <name>
       <surname>
        Iwasaki
       </surname>
       <given-names>
        K
       </given-names>
      </name>
      <name>
       <surname>
        Sato
       </surname>
       <given-names>
        C
       </given-names>
      </name>
     </person-group>
     <year iso-8601-date="2003">
      2003
     </year>
     <article-title>
      Topology representing network enables highly accurate classification of protein images taken by cryo electron-microscope without masking
     </article-title>
     <source>
      Journal of Structural Biology
     </source>
     <volume>
      143
     </volume>
     <fpage>
      185
     </fpage>
     <lpage>
      200
     </lpage>
     <pub-id pub-id-type="doi">
      10.1016/j.jsb.2003.08.005
     </pub-id>
    </element-citation>
   </ref>
   <ref id="bib28">
    <element-citation publication-type="journal">
     <person-group person-group-type="author">
      <name>
       <surname>
        Pathare
       </surname>
       <given-names>
        GR
       </given-names>
      </name>
      <name>
       <surname>
        Nagy
       </surname>
       <given-names>
        I
       </given-names>
      </name>
      <name>
       <surname>
        Sledz
       </surname>
       <given-names>
        P
       </given-names>
      </name>
      <name>
       <surname>
        Anderson
       </surname>
       <given-names>
        DJ
       </given-names>
      </name>
      <name>
       <surname>
        Zhou
       </surname>
       <given-names>
        H-J
       </given-names>
      </name>
      <name>
       <surname>
        Pardon
       </surname>
       <given-names>
        E
       </given-names>
      </name>
      <name>
       <surname>
        Steyaert
       </surname>
       <given-names>
        J
       </given-names>
      </name>
      <name>
       <surname>
        Forster
       </surname>
       <given-names>
        F
       </given-names>
      </name>
      <name>
       <surname>
        Bracher
       </surname>
       <given-names>
        A
       </given-names>
      </name>
      <name>
       <surname>
        Baumeister
       </surname>
       <given-names>
        W
       </given-names>
      </name>
     </person-group>
     <year iso-8601-date="2014">
      2014
     </year>
     <article-title>
      Crystal structure of the proteasomal deubiquitylation module Rpn8-Rpn11
     </article-title>
     <source>
      Proceedings of the National Academy of Sciences of the United States of America
     </source>
     <volume>
      111
     </volume>
     <fpage>
      2984
     </fpage>
     <lpage>
      2989
     </lpage>
     <pub-id pub-id-type="doi">
      10.1073/pnas.1400546111
     </pub-id>
    </element-citation>
   </ref>
   <ref id="bib29">
    <element-citation publication-type="journal">
     <person-group person-group-type="author">
      <name>
       <surname>
        Roseman
       </surname>
       <given-names>
        A
       </given-names>
      </name>
     </person-group>
     <year iso-8601-date="2004">
      2004
     </year>
     <article-title>
      FindEM—a fast, efficient program for automatic selection of particles from electron micrographs
     </article-title>
     <source>
      Journal of Structural Biology
     </source>
     <volume>
      145
     </volume>
     <fpage>
      91
     </fpage>
     <lpage>
      99
     </lpage>
     <pub-id pub-id-type="doi">
      10.1016/j.jsb.2003.11.007
     </pub-id>
    </element-citation>
   </ref>
   <ref id="bib30">
    <element-citation publication-type="journal">
     <person-group person-group-type="author">
      <name>
       <surname>
        Saeki
       </surname>
       <given-names>
        Y
       </given-names>
      </name>
      <name>
       <surname>
        Tanaka
       </surname>
       <given-names>
        K
       </given-names>
      </name>
     </person-group>
     <year iso-8601-date="2012">
      2012
     </year>
     <article-title>
      Assembly and function of the proteasome
     </article-title>
     <source>
      Methods in Molecular Biology
     </source>
     <volume>
      832
     </volume>
     <fpage>
      315
     </fpage>
     <lpage>
      337
     </lpage>
     <pub-id pub-id-type="doi">
      10.1007/978-1-61779-474-2_22
     </pub-id>
    </element-citation>
   </ref>
   <ref id="bib31">
    <element-citation publication-type="journal">
     <person-group person-group-type="author">
      <name>
       <surname>
        Sato
       </surname>
       <given-names>
        Y
       </given-names>
      </name>
      <name>
       <surname>
        Yoshikawa
       </surname>
       <given-names>
        A
       </given-names>
      </name>
      <name>
       <surname>
        Yamagata
       </surname>
       <given-names>
        A
       </given-names>
      </name>
      <name>
       <surname>
        Mimura
       </surname>
       <given-names>
        H
       </given-names>
      </name>
      <name>
       <surname>
        Yamashita
       </surname>
       <given-names>
        M
       </given-names>
      </name>
      <name>
       <surname>
        Ookata
       </surname>
       <given-names>
        K
       </given-names>
      </name>
      <name>
       <surname>
        Nureki
       </surname>
       <given-names>
        O
       </given-names>
      </name>
      <name>
       <surname>
        Iwai
       </surname>
       <given-names>
        K
       </given-names>
      </name>
      <name>
       <surname>
        Komada
       </surname>
       <given-names>
        M
       </given-names>
      </name>
      <name>
       <surname>
        Fukai
       </surname>
       <given-names>
        S
       </given-names>
      </name>
     </person-group>
     <year iso-8601-date="2008">
      2008
     </year>
     <article-title>
      Structural basis for specific cleavage of lys 63-linked polyubiquitin chains
     </article-title>
     <source>
      Nature
     </source>
     <volume>
      455
     </volume>
     <fpage>
      358
     </fpage>
     <lpage>
      362
     </lpage>
     <pub-id pub-id-type="doi">
      10.1038/nature07254
     </pub-id>
    </element-citation>
   </ref>
   <ref id="bib32">
    <element-citation publication-type="journal">
     <person-group person-group-type="author">
      <name>
       <surname>
        Scheres
       </surname>
       <given-names>
        SHW
       </given-names>
      </name>
     </person-group>
     <year iso-8601-date="2012">
      2012
     </year>
     <article-title>
      RELION: implementation of a bayesian approach to cryo-EM structure determination
     </article-title>
     <source>
      Journal of Structural Biology
     </source>
     <volume>
      180
     </volume>
     <fpage>
      519
     </fpage>
     <lpage>
      530
     </lpage>
     <pub-id pub-id-type="doi">
      10.1016/j.jsb.2012.09.006
     </pub-id>
    </element-citation>
   </ref>
   <ref id="bib33">
    <element-citation publication-type="journal">
     <person-group person-group-type="author">
      <name>
       <surname>
        Shrestha
       </surname>
       <given-names>
        RK
       </given-names>
      </name>
      <name>
       <surname>
        Ronau
       </surname>
       <given-names>
        JA
       </given-names>
      </name>
      <name>
       <surname>
        Davies
       </surname>
       <given-names>
        CW
       </given-names>
      </name>
      <name>
       <surname>
        Guenette
       </surname>
       <given-names>
        RG
       </given-names>
      </name>
      <name>
       <surname>
        Strieter
       </surname>
       <given-names>
        ER
       </given-names>
      </name>
      <name>
       <surname>
        Paul
       </surname>
       <given-names>
        LN
       </given-names>
      </name>
      <name>
       <surname>
        Das
       </surname>
       <given-names>
        C
       </given-names>
      </name>
     </person-group>
     <year iso-8601-date="2014">
      2014
     </year>
     <article-title>
      Insights into the mechanism of deubiquitination by JAMM deubiquitinases from cocrystal structures of the enzyme with the substrate and product
     </article-title>
     <source>
      Biochemistry
     </source>
     <volume>
      53
     </volume>
     <fpage>
      3199
     </fpage>
     <lpage>
      3217
     </lpage>
     <pub-id pub-id-type="doi">
      10.1021/bi5003162
     </pub-id>
    </element-citation>
   </ref>
   <ref id="bib34">
    <element-citation publication-type="journal">
     <person-group person-group-type="author">
      <name>
       <surname>
        Suloway
       </surname>
       <given-names>
        C
       </given-names>
      </name>
      <name>
       <surname>
        Pulokas
       </surname>
       <given-names>
        J
       </given-names>
      </name>
      <name>
       <surname>
        Fellmann
       </surname>
       <given-names>
        D
       </given-names>
      </name>
      <name>
       <surname>
        Cheng
       </surname>
       <given-names>
        A
       </given-names>
      </name>
      <name>
       <surname>
        Guerra
       </surname>
       <given-names>
        F
       </given-names>
      </name>
      <name>
       <surname>
        Quispe
       </surname>
       <given-names>
        J
       </given-names>
      </name>
      <name>
       <surname>
        Stagg
       </surname>
       <given-names>
        S
       </given-names>
      </name>
      <name>
       <surname>
        Potter
       </surname>
       <given-names>
        CS
       </given-names>
      </name>
      <name>
       <surname>
        Carragher
       </surname>
       <given-names>
        B
       </given-names>
      </name>
     </person-group>
     <year iso-8601-date="2005">
      2005
     </year>
     <article-title>
      Automated molecular microscopy: the new leginon system
     </article-title>
     <source>
      Journal of Structural Biology
     </source>
     <volume>
      151
     </volume>
     <fpage>
      41
     </fpage>
     <lpage>
      60
     </lpage>
     <pub-id pub-id-type="doi">
      10.1016/j.jsb.2005.03.010
     </pub-id>
    </element-citation>
   </ref>
   <ref id="bib35">
    <element-citation publication-type="journal">
     <person-group person-group-type="author">
      <name>
       <surname>
        Tomko
       </surname>
       <given-names>
        RJ
       </given-names>
      </name>
      <name>
       <surname>
        Hochstrasser
       </surname>
       <given-names>
        M
       </given-names>
      </name>
     </person-group>
     <year iso-8601-date="2011">
      2011
     </year>
     <article-title>
      Incorporation of the Rpn12 subunit couples completion of proteasome regulatory particle lid assembly to lid-base joining
     </article-title>
     <source>
      Molecular Cell
     </source>
     <volume>
      44
     </volume>
     <fpage>
      907
     </fpage>
     <lpage>
      917
     </lpage>
     <pub-id pub-id-type="doi">
      10.1016/j.molcel.2011.11.020
     </pub-id>
    </element-citation>
   </ref>
   <ref id="bib36">
    <element-citation publication-type="journal">
     <person-group person-group-type="author">
      <name>
       <surname>
        Tomko
       </surname>
       <given-names>
        RJ
       </given-names>
      </name>
      <name>
       <surname>
        Taylor
       </surname>
       <given-names>
        DW
       </given-names>
      </name>
      <name>
       <surname>
        Chen
       </surname>
       <given-names>
        ZA
       </given-names>
      </name>
      <name>
       <surname>
        Wang
       </surname>
       <given-names>
        H-W
       </given-names>
      </name>
      <name>
       <surname>
        Rappsilber
       </surname>
       <given-names>
        J
       </given-names>
      </name>
      <name>
       <surname>
        Hochstrasser
       </surname>
       <given-names>
        M
       </given-names>
      </name>
     </person-group>
     <year iso-8601-date="2015">
      2015
     </year>
     <article-title>
      A single α helix drives extensive remodeling of the proteasome lid and completion of regulatory particle assembly
     </article-title>
     <source>
      Cell
     </source>
     <volume>
      163
     </volume>
     <fpage>
      432
     </fpage>
     <lpage>
      444
     </lpage>
     <pub-id pub-id-type="doi">
      10.1016/j.cell.2015.09.022
     </pub-id>
    </element-citation>
   </ref>
   <ref id="bib37">
    <element-citation publication-type="journal">
     <person-group person-group-type="author">
      <name>
       <surname>
        Unverdorben
       </surname>
       <given-names>
        P
       </given-names>
      </name>
      <name>
       <surname>
        Beck
       </surname>
       <given-names>
        F
       </given-names>
      </name>
      <name>
       <surname>
        led
       </surname>
       <given-names>
        P
       </given-names>
      </name>
      <name>
       <surname>
        Schweitzer
       </surname>
       <given-names>
        A
       </given-names>
      </name>
      <name>
       <surname>
        Pfeifer
       </surname>
       <given-names>
        G
       </given-names>
      </name>
      <name>
       <surname>
        Plitzko
       </surname>
       <given-names>
        JM
       </given-names>
      </name>
      <name>
       <surname>
        Baumeister
       </surname>
       <given-names>
        W
       </given-names>
      </name>
      <name>
       <surname>
        Forster
       </surname>
       <given-names>
        F
       </given-names>
      </name>
     </person-group>
     <year iso-8601-date="2014">
      2014
     </year>
     <article-title>
      Deep classification of a large cryo-EM dataset defines the conformational landscape of the 26S proteasome
     </article-title>
     <source>
      Proceedings of the National Academy of Sciences of the United States of America
     </source>
     <volume>
      111
     </volume>
     <fpage>
      5544
     </fpage>
     <lpage>
      5549
     </lpage>
     <pub-id pub-id-type="doi">
      10.1073/pnas.1403409111
     </pub-id>
    </element-citation>
   </ref>
   <ref id="bib38">
    <element-citation publication-type="journal">
     <person-group person-group-type="author">
      <name>
       <surname>
        Verma
       </surname>
       <given-names>
        R
       </given-names>
      </name>
      <name>
       <surname>
        Aravind
       </surname>
       <given-names>
        L
       </given-names>
      </name>
      <name>
       <surname>
        Oania
       </surname>
       <given-names>
        R
       </given-names>
      </name>
      <name>
       <surname>
        McDonald
       </surname>
       <given-names>
        WH
       </given-names>
      </name>
      <name>
       <surname>
        Yates
       </surname>
       <given-names>
        JR
       </given-names>
      </name>
      <name>
       <surname>
        Koonin
       </surname>
       <given-names>
        EV
       </given-names>
      </name>
      <name>
       <surname>
        Deshaies
       </surname>
       <given-names>
        RJ
       </given-names>
      </name>
     </person-group>
     <year iso-8601-date="2002">
      2002
     </year>
     <article-title>
      Role of Rpn11 metalloprotease in deubiquitination and degradation by the 26S proteasome
     </article-title>
     <source>
      Science
     </source>
     <volume>
      298
     </volume>
     <fpage>
      611
     </fpage>
     <lpage>
      615
     </lpage>
     <pub-id pub-id-type="doi">
      10.1126/science.1075898
     </pub-id>
    </element-citation>
   </ref>
   <ref id="bib39">
    <element-citation publication-type="journal">
     <person-group person-group-type="author">
      <name>
       <surname>
        Voss
       </surname>
       <given-names>
        NR
       </given-names>
      </name>
      <name>
       <surname>
        Yoshioka
       </surname>
       <given-names>
        CK
       </given-names>
      </name>
      <name>
       <surname>
        Radermacher
       </surname>
       <given-names>
        M
       </given-names>
      </name>
      <name>
       <surname>
        Potter
       </surname>
       <given-names>
        CS
       </given-names>
      </name>
      <name>
       <surname>
        Carragher
       </surname>
       <given-names>
        B
       </given-names>
      </name>
     </person-group>
     <year iso-8601-date="2009">
      2009
     </year>
     <article-title>
      DoG picker and TiltPicker: software tools to facilitate particle selection in single particle electron microscopy
     </article-title>
     <source>
      Journal of Structural Biology
     </source>
     <volume>
      166
     </volume>
     <fpage>
      205
     </fpage>
     <lpage>
      213
     </lpage>
     <pub-id pub-id-type="doi">
      10.1016/j.jsb.2009.01.004
     </pub-id>
    </element-citation>
   </ref>
   <ref id="bib40">
    <element-citation publication-type="journal">
     <person-group person-group-type="author">
      <name>
       <surname>
        Worden
       </surname>
       <given-names>
        EJ
       </given-names>
      </name>
      <name>
       <surname>
        Padovani
       </surname>
       <given-names>
        C
       </given-names>
      </name>
      <name>
       <surname>
        Martin
       </surname>
       <given-names>
        A
       </given-names>
      </name>
     </person-group>
     <year iso-8601-date="2014">
      2014
     </year>
     <article-title>
      Structure of the Rpn11–Rpn8 dimer reveals mechanisms of substrate deubiquitination during proteasomal degradation
     </article-title>
     <source>
      Nature Structural &amp; Molecular Biology
     </source>
     <volume>
      21
     </volume>
     <fpage>
      220
     </fpage>
     <lpage>
      227
     </lpage>
     <pub-id pub-id-type="doi">
      10.1038/nsmb.2771
     </pub-id>
    </element-citation>
   </ref>
   <ref id="bib41">
    <element-citation publication-type="journal">
     <person-group person-group-type="author">
      <name>
       <surname>
        Yao
       </surname>
       <given-names>
        T
       </given-names>
      </name>
      <name>
       <surname>
        Cohen
       </surname>
       <given-names>
        RE
       </given-names>
      </name>
     </person-group>
     <year iso-8601-date="2002">
      2002
     </year>
     <article-title>
      A cryptic protease couples deubiquitination and degradation by the proteasome
     </article-title>
     <source>
      Nature
     </source>
     <volume>
      419
     </volume>
     <fpage>
      403
     </fpage>
     <lpage>
      407
     </lpage>
     <pub-id pub-id-type="doi">
      10.1038/nature01071
     </pub-id>
    </element-citation>
   </ref>
  </ref-list>
 </back>
 <sub-article article-type="article-commentary" id="SA1">
  <front-stub>
   <article-id pub-id-type="doi">
    10.7554/eLife.13027.025
   </article-id>
   <title-group>
    <article-title>
     Decision letter
    </article-title>
   </title-group>
   <contrib-group content-type="section">
    <contrib contrib-type="editor">
     <name>
      <surname>
       Scheres
      </surname>
      <given-names>
       Sjors HW
      </given-names>
     </name>
     <role>
      Reviewing editor
     </role>
     <aff id="aff6">
      <institution>
       Medical Research Council
      </institution>
      ,
      <country>
       United Kingdom
      </country>
     </aff>
    </contrib>
   </contrib-group>
  </front-stub>
  <body>
   <boxed-text>
    <p>
     In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.
    </p>
   </boxed-text>
   <p>
    Thank you for submitting your work entitled "Atomic structure of the 26S proteasome lid shows the mechanism of deubiquitinase inhibition" for consideration by
    <italic>
     eLife
    </italic>
    . Your article has been favorably evaluated by Ivan Dikic (Senior editor) and three reviewers, one of whom, Sjors Scheres, is a member of our Board of Reviewing Editors. The following individual involved in review of your submission has agreed to reveal their identity: David Barford (peer reviewer). A further reviewer remains anonymous.
   </p>
   <p>
    The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.
   </p>
   <p>
    Summary:
   </p>
   <p>
    This paper describes a near-atomic resolution cryo-EM structure of the free lid sub-complex from the 26S proteasome. The 26 S proteasome mediates the ubiquitin-dependent proteolysis of many regulatory and unfolded proteins. It plays essential roles in virtually all biological processes. Thus structural and mechanistic studies of this large and highly complex macromolecular assembly are extremely important. The main interest of the free lid sub-complex is to see how it compares to the structure of the lid in the context of the mature 26S proteasome, which is known from previous near-atomic resolution cryo-EM structures. Most significantly, the structure helps to rationalize why the Rpn11 ubiquitin isopeptidase is nearly inactive in the free lid as a result of conformational and steric obstruction of the Rpn11 active site, especially by the N-terminal domain of Rpn5. This is supported by mutational and enzymatic activity analyses.
   </p>
   <p>
    The paper is well written and deemed appropriate for publication in
    <italic>
     eLife
    </italic>
    , provided the essential revisions below are addressed adequately.
   </p>
   <p>
    Essential revisions:
   </p>
   <p>
    It would be useful to mention if the crosslinking analysis recently done on the lid, as reported in Cell 163:432-44, is consistent with the cryo-EM and mutational data in the current work. It should at least be cited as a previous method used to analyze lid structure and its changes upon engagement with the full proteasome since this earlier report also indicated large conformational changes between free and engaged lid.
   </p>
   <p>
    At 3.5 Angstrom resolution one cannot see individual water molecules! Therefore, the discussion in the subsection “Rpn5 occludes the Rpn11 active site” regarding the water molecule should be carefully reworded. The other crystal structures of Zn-associated water molecules can provide suggestions that water is also present in this structure, but the current experimental data do
    <italic>
     not
    </italic>
    indicate that water is present in this structure.
   </p>
  </body>
 </sub-article>
 <sub-article article-type="reply" id="SA2">
  <front-stub>
   <article-id pub-id-type="doi">
    10.7554/eLife.13027.026
   </article-id>
   <title-group>
    <article-title>
     Author response
    </article-title>
   </title-group>
  </front-stub>
  <body>
   <p>
    <italic>
     This paper describes a near-atomic resolution cryo-EM structure of the free lid sub-complex from the 26S proteasome. The 26 S proteasome mediates the ubiquitin-dependent proteolysis of many regulatory and unfolded proteins. It plays essential roles in virtually all biological processes. Thus structural and mechanistic studies of this large and highly complex macromolecular assembly are extremely important. The main interest of the free lid sub-complex is to see how it compares to the structure of the lid in the context of the mature 26S proteasome, which is known from previous near-atomic resolution cryo-EM structures. Most significantly, the structure helps to rationalize why the Rpn11 ubiquitin isopeptidase is nearly inactive in the free lid as a result of conformational and steric obstruction of the Rpn11 active site, especially by the N-terminal domain of Rpn5. This is supported by mutational and enzymatic activity analyses. The paper is well written and deemed appropriate for publication in
    </italic>
    eLife
   </p>
   <p>
    <italic>
     , provided the essential revisions below are addressed adequately.
    </italic>
   </p>
   <p>
    We thank the reviewers for their assessment of the manuscript. We feel obliged, however, to point out that the mature 26S proteasome is
    <italic>
     not
    </italic>
    known to near-atomic resolution. Currently, the highest resolution structure of the 26S proteasome is around 7 Å, which is far from near-atomic.
   </p>
   <p>
    We have made the requested changes to the manuscript, as explained below.
   </p>
   <p>
    <italic>
     Essential revisions: It would be useful to mention if the crosslinking analysis recently done on the lid, as reported in Cell 163:432-44, is consistent with the cryo-EM and mutational data in the current work. It should at least be cited as a previous method used to analyze lid structure and its changes upon engagement with the full proteasome since this earlier report also indicated large conformational changes between free and engaged lid.
    </italic>
   </p>
   <p>
    We discuss the results of the crosslinking study in light of our work in the first paragraph of the “Lid architecture” section.
   </p>
   <p>
    <italic>
     At 3.5 Angstrom resolution one cannot see individual water molecules! Therefore, the discussion in the subsection “Rpn5 occludes the Rpn11 active site” regarding the water molecule should be carefully reworded. The other crystal structures of Zn-associated water molecules can provide suggestions that water is also present in this structure, but the current experimental data do not indicate that water is present in this structure.
    </italic>
   </p>
   <p>
    Upon re-reading this section of the manuscript, we agree that we overstated our ability to interpret the electron density as a water molecule. However, this region of the map is closer to 3Å resolution, and although we don’t observe a well-defined punctate density corresponding to a water molecule, we do see an extension of the EM density between the Zn and the Asn275, and we think it’s appropriate to mention that the density is consistent with the previously observed Zn-associated water molecule in crystallographic studies. We have, as suggested, substantially softened the language regarding this density (subsection “Rpn5 occludes the Rpn11 active site”, last paragraph).
   </p>
  </body>
 </sub-article>
</article>
        ''').strip('\n')