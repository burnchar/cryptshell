The cipher analyzed is a substitution cipher.  The text was originally found at http://www.simonsingh.net/Stage_1.html

# Introduction #

First, load the file 'test' into cryptshell like the following:

```
$cryptshell test
```

where test contains the following text

```
BT JPX RMLX PCUV AMLX ICVJP IBTWXVR CI M LMT’R PMTN, MTN YVCJX CDXV MWMBTRJ JPX AMTNGXRJBAH UQCT JPX QGMRJXV CI JPX YMGG CI JPX HBTW’R QMGMAX; MTN JPX HBTW RMY JPX QMVJ CI JPX PMTN JPMJ YVCJX. JPXT JPX HBTW’R ACUTJXTMTAX YMR APMTWXN, MTN PBR JPCUWPJR JVCUFGXN PBL, RC JPMJ JPX SCBTJR CI PBR GCBTR YXVX GCCRXN, MTN PBR HTXXR RLCJX CTX MWMBTRJ MTCJPXV. JPX HBTW AVBXN MGCUN JC FVBTW BT JPX MRJVCGCWXVR, JPX APMGNXMTR, MTN JPX RCCJPRMEXVR. MTN JPX HBTW RQMHX, MTN RMBN JC JPX YBRX LXT CI FMFEGCT, YPCRCXDXV RPMGG VXMN JPBR YVBJBTW, MTN RPCY LX JPX BTJXVQVXJMJBCT JPXVXCI, RPMGG FX AGCJPXN YBJP RAMVGXJ, MTN PMDX M APMBT CI WCGN MFCUJ PBR TXAH, MTN RPMGG FX JPX JPBVN VUGXV BT JPX HBTWNCL. JPXT AMLX BT MGG JPX HBTW’R YBRX LXT; FUJ JPXE ACUGN TCJ VXMN JPX YVBJBTW, TCV LMHX HTCYT JC JPX HBTW JPX BTJXVQVXJMJBCT JPXVXCI. JPXT YMR HBTW FXGRPMOOMV WVXMJGE JVCUFGXN, MTN PBR ACUTJXTMTAX YMR APMTWXN BT PBL, MTN PBR GCVNR YXVX MRJCTBRPXN. TCY JPX KUXXT, FE VXMRCT CI JPX YCVNR CI JPX HBTW MTN PBR GCVNR, AMLX BTJC JPX FMTKUXJ PCURX; MTN JPX KUXXT RQMHX MTN RMBN, C HBTW, GBDX ICVXDXV; GXJ TCJ JPE JPCUWPJR JVCUFGX JPXX, TCV GXJ JPE ACUTJXTMTAX FX APMTWXN; JPXVX BR M LMT BT JPE HBTWNCL, BT YPCL BR JPX RQBVBJ CI JPX PCGE WCNR; MTN BT JPX NMER CI JPE IMJPXV GBWPJ MTN UTNXVRJMTNBTW MTN YBRNCL, GBHX JPX YBRNCL CI JPX WCNR, YMR ICUTN BT PBL; YPCL JPX HBTW TXFUAPMNTXOOMV JPE IMJPXV, JPX HBTW, B RME, JPE IMJPXV, LMNX LMRJXV CI JPX LMWBABMTR, MRJVCGCWXVR, APMGNXMTR, MTN RCCJPRMEXVR; ICVMRLUAP MR MT XZAXGGXTJ RQBVBJ, MTN HTCYGXNWX, MTN UTNXVRJMTNBTW, BTJXVQVXJBTW CI NVXMLR, MTN RPCYBTW CI PMVN RXTJXTAXR, MTN NBRRCGDBTW CI NCUFJR, YXVX ICUTN BT JPX RMLX NMTBXG, YPCL JPX HBTW TMLXN FXGJXRPMOOMV; TCY GXJ NMTBXG FX AMGGXN, MTN PX YBGG RPCY JPX BTJXVQVXJMJBCT. JPX IBVRJ ACNXYCVN BR CJPXGGC.

```

```
WWW         WW eEeEeEeE LL        CCCCC    OOOO    MMMM    MMMM  eEeEeEeE
 WW         W  EE       LL       Cc      OOO  OOO  MM MM  M  MM  EE
  WW       WW  EeEeE    LL      CC       OO    OO  MM  MMM   MM  EeEeE
  WWw WW  WW   EE       LL       Cc      OOO  OOO  MM        MM  EE
   WWW  WWW    eEeEeEeE LlLlLlL   CCCCC    OOOO    MM        MM  eEeEeEeE
  
                             TO CRYPTO-SHELL
  (Useful for deciphering what little Susie is writing to little Billy)

>
```

The first command to try is 'print current' which will print the current ciphertext.

```
> print current
BT JPX RMLX PCUV AMLX ICVJP IBTWXVR CI M LMT’R PMTN, MTN YVCJX CDXV MWMBTRJ JPX AMTNGXRJBAH UQCT JPX QGMRJXV CI JPX YMGG CI JPX HBTW’R QMGMAX; MTN JPX HBTW RMY JPX QMVJ CI JPX PMTN JPMJ YVCJX. JPXT JPX HBTW’R ACUTJXTMTAX YMR APMTWXN, MTN PBR JPCUWPJR JVCUFGXN PBL, RC JPMJ JPX SCBTJR CI PBR GCBTR YXVX GCCRXN, MTN PBR HTXXR RLCJX CTX MWMBTRJ MTCJPXV. JPX HBTW AVBXN MGCUN JC FVBTW BT JPX MRJVCGCWXVR, JPX APMGNXMTR, MTN JPX RCCJPRMEXVR. MTN JPX HBTW RQMHX, MTN RMBN JC JPX YBRX LXT CI FMFEGCT, YPCRCXDXV RPMGG VXMN JPBR YVBJBTW, MTN RPCY LX JPX BTJXVQVXJMJBCT JPXVXCI, RPMGG FX AGCJPXN YBJP RAMVGXJ, MTN PMDX M APMBT CI WCGN MFCUJ PBR TXAH, MTN RPMGG FX JPX JPBVN VUGXV BT JPX HBTWNCL. JPXT AMLX BT MGG JPX HBTW’R YBRX LXT; FUJ JPXE ACUGN TCJ VXMN JPX YVBJBTW, TCV LMHX HTCYT JC JPX HBTW JPX BTJXVQVXJMJBCT JPXVXCI. JPXT YMR HBTW FXGRPMOOMV WVXMJGE JVCUFGXN, MTN PBR ACUTJXTMTAX YMR APMTWXN BT PBL, MTN PBR GCVNR YXVX MRJCTBRPXN. TCY JPX KUXXT, FE VXMRCT CI JPX YCVNR CI JPX HBTW MTN PBR GCVNR, AMLX BTJC JPX FMTKUXJ PCURX; MTN JPX KUXXT RQMHX MTN RMBN, C HBTW, GBDX ICVXDXV; GXJ TCJ JPE JPCUWPJR JVCUFGX JPXX, TCV GXJ JPE ACUTJXTMTAX FX APMTWXN; JPXVX BR M LMT BT JPE HBTWNCL, BT YPCL BR JPX RQBVBJ CI JPX PCGE WCNR; MTN BT JPX NMER CI JPE IMJPXV GBWPJ MTN UTNXVRJMTNBTW MTN YBRNCL, GBHX JPX YBRNCL CI JPX WCNR, YMR ICUTN BT PBL; YPCL JPX HBTW TXFUAPMNTXOOMV JPE IMJPXV, JPX HBTW, B RME, JPE IMJPXV, LMNX LMRJXV CI JPX LMWBABMTR, MRJVCGCWXVR, APMGNXMTR, MTN RCCJPRMEXVR; ICVMRLUAP MR MT XZAXGGXTJ RQBVBJ, MTN HTCYGXNWX, MTN UTNXVRJMTNBTW, BTJXVQVXJBTW CI NVXMLR, MTN RPCYBTW CI PMVN RXTJXTAXR, MTN NBRRCGDBTW CI NCUFJR, YXVX ICUTN BT JPX RMLX NMTBXG, YPCL JPX HBTW TMLXN FXGJXRPMOOMV; TCY GXJ NMTBXG FX AMGGXN, MTN PX YBGG RPCY JPX BTJXVQVXJMJBCT. JPX IBVRJ ACNXYCVN BR CJPXGGC.
```

Now, if we want to see a frequency analysis, we can type 'print graph' (for this functionality you need Linux and gtk- alternatively you can print freq which gives a textual representation).

```
> print graph
```

This prints the following graph:

![http://cryptshell.googlecode.com/svn/wiki/images/sub_1.png](http://cryptshell.googlecode.com/svn/wiki/images/sub_1.png)


The next step is to perform some substitutions.  A good place to start would be to substitute X for e since they are the most common.

```
> sub X e
> print current
BT JPe RMLe PCUV AMLe ICVJP IBTWeVR CI M LMT’R PMTN, MTN YVCJe CDeV MWMBTRJ JPe AMTNGeRJBAH UQCT JPe QGMRJeV CI JPe YMGG CI JPe HBTW’R QMGMAe; MTN JPe HBTW RMY JPe QMVJ CI JPe PMTN JPMJ YVCJe. JPeT JPe HBTW’R ACUTJeTMTAe YMR APMTWeN, MTN PBR JPCUWPJR JVCUFGeN PBL, RC JPMJ JPe SCBTJR CI PBR GCBTR YeVe GCCReN, MTN PBR HTeeR RLCJe CTe MWMBTRJ MTCJPeV. JPe HBTW AVBeN MGCUN JC FVBTW BT JPe MRJVCGCWeVR, JPe APMGNeMTR, MTN JPe RCCJPRMEeVR. MTN JPe HBTW RQMHe, MTN RMBN JC JPe YBRe LeT CI FMFEGCT, YPCRCeDeV RPMGG VeMN JPBR YVBJBTW, MTN RPCY Le JPe BTJeVQVeJMJBCT JPeVeCI, RPMGG Fe AGCJPeN YBJP RAMVGeJ, MTN PMDe M APMBT CI WCGN MFCUJ PBR TeAH, MTN RPMGG Fe JPe JPBVN VUGeV BT JPe HBTWNCL. JPeT AMLe BT MGG JPe HBTW’R YBRe LeT; FUJ JPeE ACUGN TCJ VeMN JPe YVBJBTW, TCV LMHe HTCYT JC JPe HBTW JPe BTJeVQVeJMJBCT JPeVeCI. JPeT YMR HBTW FeGRPMOOMV WVeMJGE JVCUFGeN, MTN PBR ACUTJeTMTAe YMR APMTWeN BT PBL, MTN PBR GCVNR YeVe MRJCTBRPeN. TCY JPe KUeeT, FE VeMRCT CI JPe YCVNR CI JPe HBTW MTN PBR GCVNR, AMLe BTJC JPe FMTKUeJ PCURe; MTN JPe KUeeT RQMHe MTN RMBN, C HBTW, GBDe ICVeDeV; GeJ TCJ JPE JPCUWPJR JVCUFGe JPee, TCV GeJ JPE ACUTJeTMTAe Fe APMTWeN; JPeVe BR M LMT BT JPE HBTWNCL, BT YPCL BR JPe RQBVBJ CI JPe PCGE WCNR; MTN BT JPe NMER CI JPE IMJPeV GBWPJ MTN UTNeVRJMTNBTW MTN YBRNCL, GBHe JPe YBRNCL CI JPe WCNR, YMR ICUTN BT PBL; YPCL JPe HBTW TeFUAPMNTeOOMV JPE IMJPeV, JPe HBTW, B RME, JPE IMJPeV, LMNe LMRJeV CI JPe LMWBABMTR, MRJVCGCWeVR, APMGNeMTR, MTN RCCJPRMEeVR; ICVMRLUAP MR MT eZAeGGeTJ RQBVBJ, MTN HTCYGeNWe, MTN UTNeVRJMTNBTW, BTJeVQVeJBTW CI NVeMLR, MTN RPCYBTW CI PMVN ReTJeTAeR, MTN NBRRCGDBTW CI NCUFJR, YeVe ICUTN BT JPe RMLe NMTBeG, YPCL JPe HBTW TMLeN FeGJeRPMOOMV; TCY GeJ NMTBeG Fe AMGGeN, MTN Pe YBGG RPCY JPe BTJeVQVeJMJBCT. JPe IBVRJ ACNeYCVN BR CJPeGGC.
```

Now notice the "JPe" string.  Since "the" is very common, we guess that J is t and P is h.

```
> sub P h
> sub J t
> print current
BT the RMLe hCUV AMLe ICVth IBTWeVR CI M LMT’R hMTN, MTN YVCte CDeV MWMBTRt the AMTNGeRtBAH UQCT the QGMRteV CI the YMGG CI the HBTW’R QMGMAe; MTN the HBTW RMY the QMVt CI the hMTN thMt YVCte. theT the HBTW’R ACUTteTMTAe YMR AhMTWeN, MTN hBR thCUWhtR tVCUFGeN hBL, RC thMt the SCBTtR CI hBR GCBTR YeVe GCCReN, MTN hBR HTeeR RLCte CTe MWMBTRt MTCtheV. the HBTW AVBeN MGCUN tC FVBTW BT the MRtVCGCWeVR, the AhMGNeMTR, MTN the RCCthRMEeVR. MTN the HBTW RQMHe, MTN RMBN tC the YBRe LeT CI FMFEGCT, YhCRCeDeV RhMGG VeMN thBR YVBtBTW, MTN RhCY Le the BTteVQVetMtBCT theVeCI, RhMGG Fe AGCtheN YBth RAMVGet, MTN hMDe M AhMBT CI WCGN MFCUt hBR TeAH, MTN RhMGG Fe the thBVN VUGeV BT the HBTWNCL. theT AMLe BT MGG the HBTW’R YBRe LeT; FUt theE ACUGN TCt VeMN the YVBtBTW, TCV LMHe HTCYT tC the HBTW the BTteVQVetMtBCT theVeCI. theT YMR HBTW FeGRhMOOMV WVeMtGE tVCUFGeN, MTN hBR ACUTteTMTAe YMR AhMTWeN BT hBL, MTN hBR GCVNR YeVe MRtCTBRheN. TCY the KUeeT, FE VeMRCT CI the YCVNR CI the HBTW MTN hBR GCVNR, AMLe BTtC the FMTKUet hCURe; MTN the KUeeT RQMHe MTN RMBN, C HBTW, GBDe ICVeDeV; Get TCt thE thCUWhtR tVCUFGe thee, TCV Get thE ACUTteTMTAe Fe AhMTWeN; theVe BR M LMT BT thE HBTWNCL, BT YhCL BR the RQBVBt CI the hCGE WCNR; MTN BT the NMER CI thE IMtheV GBWht MTN UTNeVRtMTNBTW MTN YBRNCL, GBHe the YBRNCL CI the WCNR, YMR ICUTN BT hBL; YhCL the HBTW TeFUAhMNTeOOMV thE IMtheV, the HBTW, B RME, thE IMtheV, LMNe LMRteV CI the LMWBABMTR, MRtVCGCWeVR, AhMGNeMTR, MTN RCCthRMEeVR; ICVMRLUAh MR MT eZAeGGeTt RQBVBt, MTN HTCYGeNWe, MTN UTNeVRtMTNBTW, BTteVQVetBTW CI NVeMLR, MTN RhCYBTW CI hMVN ReTteTAeR, MTN NBRRCGDBTW CI NCUFtR, YeVe ICUTN BT the RMLe NMTBeG, YhCL the HBTW TMLeN FeGteRhMOOMV; TCY Get NMTBeG Fe AMGGeN, MTN he YBGG RhCY the BTteVQVetMtBCT. the IBVRt ACNeYCVN BR CtheGGC.
```

This gives some promising clues.  It  also suggests that the spacing is probably correct.  Next we can try M as 'a' since there are very few single letter words in english.

```
> sub M a
> print current
BT the RaLe hCUV AaLe ICVth IBTWeVR CI a LaT’R haTN, aTN YVCte CDeV aWaBTRt the AaTNGeRtBAH UQCT the QGaRteV CI the YaGG CI the HBTW’R QaGaAe; aTN the HBTW RaY the QaVt CI the haTN that YVCte. theT the HBTW’R ACUTteTaTAe YaR AhaTWeN, aTN hBR thCUWhtR tVCUFGeN hBL, RC that the SCBTtR CI hBR GCBTR YeVe GCCReN, aTN hBR HTeeR RLCte CTe aWaBTRt aTCtheV. the HBTW AVBeN aGCUN tC FVBTW BT the aRtVCGCWeVR, the AhaGNeaTR, aTN the RCCthRaEeVR. aTN the HBTW RQaHe, aTN RaBN tC the YBRe LeT CI FaFEGCT, YhCRCeDeV RhaGG VeaN thBR YVBtBTW, aTN RhCY Le the BTteVQVetatBCT theVeCI, RhaGG Fe AGCtheN YBth RAaVGet, aTN haDe a AhaBT CI WCGN aFCUt hBR TeAH, aTN RhaGG Fe the thBVN VUGeV BT the HBTWNCL. theT AaLe BT aGG the HBTW’R YBRe LeT; FUt theE ACUGN TCt VeaN the YVBtBTW, TCV LaHe HTCYT tC the HBTW the BTteVQVetatBCT theVeCI. theT YaR HBTW FeGRhaOOaV WVeatGE tVCUFGeN, aTN hBR ACUTteTaTAe YaR AhaTWeN BT hBL, aTN hBR GCVNR YeVe aRtCTBRheN. TCY the KUeeT, FE VeaRCT CI the YCVNR CI the HBTW aTN hBR GCVNR, AaLe BTtC the FaTKUet hCURe; aTN the KUeeT RQaHe aTN RaBN, C HBTW, GBDe ICVeDeV; Get TCt thE thCUWhtR tVCUFGe thee, TCV Get thE ACUTteTaTAe Fe AhaTWeN; theVe BR a LaT BT thE HBTWNCL, BT YhCL BR the RQBVBt CI the hCGE WCNR; aTN BT the NaER CI thE IatheV GBWht aTN UTNeVRtaTNBTW aTN YBRNCL, GBHe the YBRNCL CI the WCNR, YaR ICUTN BT hBL; YhCL the HBTW TeFUAhaNTeOOaV thE IatheV, the HBTW, B RaE, thE IatheV, LaNe LaRteV CI the LaWBABaTR, aRtVCGCWeVR, AhaGNeaTR, aTN RCCthRaEeVR; ICVaRLUAh aR aT eZAeGGeTt RQBVBt, aTN HTCYGeNWe, aTN UTNeVRtaTNBTW, BTteVQVetBTW CI NVeaLR, aTN RhCYBTW CI haVN ReTteTAeR, aTN NBRRCGDBTW CI NCUFtR, YeVe ICUTN BT the RaLe NaTBeG, YhCL the HBTW TaLeN FeGteRhaOOaV; TCY Get NaTBeG Fe AaGGeN, aTN he YBGG RhCY the BTteVQVetatBCT. the IBVRt ACNeYCVN BR CtheGGC.
```

Since there is a thE, and E is not E, the E is probably 'y' making the word 'thy'

```
> sub E y
> print current
BT the RaLe hCUV AaLe ICVth IBTWeVR CI a LaT’R haTN, aTN YVCte CDeV aWaBTRt the AaTNGeRtBAH UQCT the QGaRteV CI the YaGG CI the HBTW’R QaGaAe; aTN the HBTW RaY the QaVt CI the haTN that YVCte. theT the HBTW’R ACUTteTaTAe YaR AhaTWeN, aTN hBR thCUWhtR tVCUFGeN hBL, RC that the SCBTtR CI hBR GCBTR YeVe GCCReN, aTN hBR HTeeR RLCte CTe aWaBTRt aTCtheV. the HBTW AVBeN aGCUN tC FVBTW BT the aRtVCGCWeVR, the AhaGNeaTR, aTN the RCCthRayeVR. aTN the HBTW RQaHe, aTN RaBN tC the YBRe LeT CI FaFyGCT, YhCRCeDeV RhaGG VeaN thBR YVBtBTW, aTN RhCY Le the BTteVQVetatBCT theVeCI, RhaGG Fe AGCtheN YBth RAaVGet, aTN haDe a AhaBT CI WCGN aFCUt hBR TeAH, aTN RhaGG Fe the thBVN VUGeV BT the HBTWNCL. theT AaLe BT aGG the HBTW’R YBRe LeT; FUt they ACUGN TCt VeaN the YVBtBTW, TCV LaHe HTCYT tC the HBTW the BTteVQVetatBCT theVeCI. theT YaR HBTW FeGRhaOOaV WVeatGy tVCUFGeN, aTN hBR ACUTteTaTAe YaR AhaTWeN BT hBL, aTN hBR GCVNR YeVe aRtCTBRheN. TCY the KUeeT, Fy VeaRCT CI the YCVNR CI the HBTW aTN hBR GCVNR, AaLe BTtC the FaTKUet hCURe; aTN the KUeeT RQaHe aTN RaBN, C HBTW, GBDe ICVeDeV; Get TCt thy thCUWhtR tVCUFGe thee, TCV Get thy ACUTteTaTAe Fe AhaTWeN; theVe BR a LaT BT thy HBTWNCL, BT YhCL BR the RQBVBt CI the hCGy WCNR; aTN BT the NayR CI thy IatheV GBWht aTN UTNeVRtaTNBTW aTN YBRNCL, GBHe the YBRNCL CI the WCNR, YaR ICUTN BT hBL; YhCL the HBTW TeFUAhaNTeOOaV thy IatheV, the HBTW, B Ray, thy IatheV, LaNe LaRteV CI the LaWBABaTR, aRtVCGCWeVR, AhaGNeaTR, aTN RCCthRayeVR; ICVaRLUAh aR aT eZAeGGeTt RQBVBt, aTN HTCYGeNWe, aTN UTNeVRtaTNBTW, BTteVQVetBTW CI NVeaLR, aTN RhCYBTW CI haVN ReTteTAeR, aTN NBRRCGDBTW CI NCUFtR, YeVe ICUTN BT the RaLe NaTBeG, YhCL the HBTW TaLeN FeGteRhaOOaV; TCY Get NaTBeG Fe AaGGeN, aTN he YBGG RhCY the BTteVQVetatBCT. the IBVRt ACNeYCVN BR CtheGGC.
```

Now, to see where we're at, we print a graph again

![http://cryptshell.googlecode.com/svn/wiki/images/sub_2.png](http://cryptshell.googlecode.com/svn/wiki/images/sub_2.png)


'and' is a very common word that starts with 'a'.  We run with this and guess that aTN might be 'and' (also the frequencies match up nicely)

```
> sub T n
> sub N d
> print current
Bn the RaLe hCUV AaLe ICVth IBnWeVR CI a Lan’R hand, and YVCte CDeV aWaBnRt the AandGeRtBAH UQCn the QGaRteV CI the YaGG CI the HBnW’R QaGaAe; and the HBnW RaY the QaVt CI the hand that YVCte. then the HBnW’R ACUntenanAe YaR AhanWed, and hBR thCUWhtR tVCUFGed hBL, RC that the SCBntR CI hBR GCBnR YeVe GCCRed, and hBR HneeR RLCte Cne aWaBnRt anCtheV. the HBnW AVBed aGCUd tC FVBnW Bn the aRtVCGCWeVR, the AhaGdeanR, and the RCCthRayeVR. and the HBnW RQaHe, and RaBd tC the YBRe Len CI FaFyGCn, YhCRCeDeV RhaGG Vead thBR YVBtBnW, and RhCY Le the BnteVQVetatBCn theVeCI, RhaGG Fe AGCthed YBth RAaVGet, and haDe a AhaBn CI WCGd aFCUt hBR neAH, and RhaGG Fe the thBVd VUGeV Bn the HBnWdCL. then AaLe Bn aGG the HBnW’R YBRe Len; FUt they ACUGd nCt Vead the YVBtBnW, nCV LaHe HnCYn tC the HBnW the BnteVQVetatBCn theVeCI. then YaR HBnW FeGRhaOOaV WVeatGy tVCUFGed, and hBR ACUntenanAe YaR AhanWed Bn hBL, and hBR GCVdR YeVe aRtCnBRhed. nCY the KUeen, Fy VeaRCn CI the YCVdR CI the HBnW and hBR GCVdR, AaLe BntC the FanKUet hCURe; and the KUeen RQaHe and RaBd, C HBnW, GBDe ICVeDeV; Get nCt thy thCUWhtR tVCUFGe thee, nCV Get thy ACUntenanAe Fe AhanWed; theVe BR a Lan Bn thy HBnWdCL, Bn YhCL BR the RQBVBt CI the hCGy WCdR; and Bn the dayR CI thy IatheV GBWht and UndeVRtandBnW and YBRdCL, GBHe the YBRdCL CI the WCdR, YaR ICUnd Bn hBL; YhCL the HBnW neFUAhadneOOaV thy IatheV, the HBnW, B Ray, thy IatheV, Lade LaRteV CI the LaWBABanR, aRtVCGCWeVR, AhaGdeanR, and RCCthRayeVR; ICVaRLUAh aR an eZAeGGent RQBVBt, and HnCYGedWe, and UndeVRtandBnW, BnteVQVetBnW CI dVeaLR, and RhCYBnW CI haVd RentenAeR, and dBRRCGDBnW CI dCUFtR, YeVe ICUnd Bn the RaLe danBeG, YhCL the HBnW naLed FeGteRhaOOaV; nCY Get danBeG Fe AaGGed, and he YBGG RhCY the BnteVQVetatBCn. the IBVRt ACdeYCVd BR CtheGGC.
```

Great! This is looking promissing.  Here we see a "Lan'R"  Because of the apostrophe, we guess that R is 's' and maybe L is 'm' to make it "man's"

```
> sub R s
> print current
Bn the saLe hCUV AaLe ICVth IBnWeVs CI a Lan’s hand, and YVCte CDeV aWaBnst the AandGestBAH UQCn the QGasteV CI the YaGG CI the HBnW’s QaGaAe; and the HBnW saY the QaVt CI the hand that YVCte. then the HBnW’s ACUntenanAe Yas AhanWed, and hBs thCUWhts tVCUFGed hBL, sC that the SCBnts CI hBs GCBns YeVe GCCsed, and hBs Hnees sLCte Cne aWaBnst anCtheV. the HBnW AVBed aGCUd tC FVBnW Bn the astVCGCWeVs, the AhaGdeans, and the sCCthsayeVs. and the HBnW sQaHe, and saBd tC the YBse Len CI FaFyGCn, YhCsCeDeV shaGG Vead thBs YVBtBnW, and shCY Le the BnteVQVetatBCn theVeCI, shaGG Fe AGCthed YBth sAaVGet, and haDe a AhaBn CI WCGd aFCUt hBs neAH, and shaGG Fe the thBVd VUGeV Bn the HBnWdCL. then AaLe Bn aGG the HBnW’s YBse Len; FUt they ACUGd nCt Vead the YVBtBnW, nCV LaHe HnCYn tC the HBnW the BnteVQVetatBCn theVeCI. then Yas HBnW FeGshaOOaV WVeatGy tVCUFGed, and hBs ACUntenanAe Yas AhanWed Bn hBL, and hBs GCVds YeVe astCnBshed. nCY the KUeen, Fy VeasCn CI the YCVds CI the HBnW and hBs GCVds, AaLe BntC the FanKUet hCUse; and the KUeen sQaHe and saBd, C HBnW, GBDe ICVeDeV; Get nCt thy thCUWhts tVCUFGe thee, nCV Get thy ACUntenanAe Fe AhanWed; theVe Bs a Lan Bn thy HBnWdCL, Bn YhCL Bs the sQBVBt CI the hCGy WCds; and Bn the days CI thy IatheV GBWht and UndeVstandBnW and YBsdCL, GBHe the YBsdCL CI the WCds, Yas ICUnd Bn hBL; YhCL the HBnW neFUAhadneOOaV thy IatheV, the HBnW, B say, thy IatheV, Lade LasteV CI the LaWBABans, astVCGCWeVs, AhaGdeans, and sCCthsayeVs; ICVasLUAh as an eZAeGGent sQBVBt, and HnCYGedWe, and UndeVstandBnW, BnteVQVetBnW CI dVeaLs, and shCYBnW CI haVd sentenAes, and dBssCGDBnW CI dCUFts, YeVe ICUnd Bn the saLe danBeG, YhCL the HBnW naLed FeGteshaOOaV; nCY Get danBeG Fe AaGGed, and he YBGG shCY the BnteVQVetatBCn. the IBVst ACdeYCVd Bs CtheGGC.

> sub L m
> print current
Bn the same hCUV Aame ICVth IBnWeVs CI a man’s hand, and YVCte CDeV aWaBnst the AandGestBAH UQCn the QGasteV CI the YaGG CI the HBnW’s QaGaAe; and the HBnW saY the QaVt CI the hand that YVCte. then the HBnW’s ACUntenanAe Yas AhanWed, and hBs thCUWhts tVCUFGed hBm, sC that the SCBnts CI hBs GCBns YeVe GCCsed, and hBs Hnees smCte Cne aWaBnst anCtheV. the HBnW AVBed aGCUd tC FVBnW Bn the astVCGCWeVs, the AhaGdeans, and the sCCthsayeVs. and the HBnW sQaHe, and saBd tC the YBse men CI FaFyGCn, YhCsCeDeV shaGG Vead thBs YVBtBnW, and shCY me the BnteVQVetatBCn theVeCI, shaGG Fe AGCthed YBth sAaVGet, and haDe a AhaBn CI WCGd aFCUt hBs neAH, and shaGG Fe the thBVd VUGeV Bn the HBnWdCm. then Aame Bn aGG the HBnW’s YBse men; FUt they ACUGd nCt Vead the YVBtBnW, nCV maHe HnCYn tC the HBnW the BnteVQVetatBCn theVeCI. then Yas HBnW FeGshaOOaV WVeatGy tVCUFGed, and hBs ACUntenanAe Yas AhanWed Bn hBm, and hBs GCVds YeVe astCnBshed. nCY the KUeen, Fy VeasCn CI the YCVds CI the HBnW and hBs GCVds, Aame BntC the FanKUet hCUse; and the KUeen sQaHe and saBd, C HBnW, GBDe ICVeDeV; Get nCt thy thCUWhts tVCUFGe thee, nCV Get thy ACUntenanAe Fe AhanWed; theVe Bs a man Bn thy HBnWdCm, Bn YhCm Bs the sQBVBt CI the hCGy WCds; and Bn the days CI thy IatheV GBWht and UndeVstandBnW and YBsdCm, GBHe the YBsdCm CI the WCds, Yas ICUnd Bn hBm; YhCm the HBnW neFUAhadneOOaV thy IatheV, the HBnW, B say, thy IatheV, made masteV CI the maWBABans, astVCGCWeVs, AhaGdeans, and sCCthsayeVs; ICVasmUAh as an eZAeGGent sQBVBt, and HnCYGedWe, and UndeVstandBnW, BnteVQVetBnW CI dVeams, and shCYBnW CI haVd sentenAes, and dBssCGDBnW CI dCUFts, YeVe ICUnd Bn the same danBeG, YhCm the HBnW named FeGteshaOOaV; nCY Get danBeG Fe AaGGed, and he YBGG shCY the BnteVQVetatBCn. the IBVst ACdeYCVd Bs CtheGGC.
```

I see a 'tC', which is probably 'to'

```
> sub C o
> print current
Bn the same hoUV Aame IoVth IBnWeVs oI a man’s hand, and YVote oDeV aWaBnst the AandGestBAH UQon the QGasteV oI the YaGG oI the HBnW’s QaGaAe; and the HBnW saY the QaVt oI the hand that YVote. then the HBnW’s AoUntenanAe Yas AhanWed, and hBs thoUWhts tVoUFGed hBm, so that the SoBnts oI hBs GoBns YeVe Goosed, and hBs Hnees smote one aWaBnst anotheV. the HBnW AVBed aGoUd to FVBnW Bn the astVoGoWeVs, the AhaGdeans, and the soothsayeVs. and the HBnW sQaHe, and saBd to the YBse men oI FaFyGon, YhosoeDeV shaGG Vead thBs YVBtBnW, and shoY me the BnteVQVetatBon theVeoI, shaGG Fe AGothed YBth sAaVGet, and haDe a AhaBn oI WoGd aFoUt hBs neAH, and shaGG Fe the thBVd VUGeV Bn the HBnWdom. then Aame Bn aGG the HBnW’s YBse men; FUt they AoUGd not Vead the YVBtBnW, noV maHe HnoYn to the HBnW the BnteVQVetatBon theVeoI. then Yas HBnW FeGshaOOaV WVeatGy tVoUFGed, and hBs AoUntenanAe Yas AhanWed Bn hBm, and hBs GoVds YeVe astonBshed. noY the KUeen, Fy Veason oI the YoVds oI the HBnW and hBs GoVds, Aame Bnto the FanKUet hoUse; and the KUeen sQaHe and saBd, o HBnW, GBDe IoVeDeV; Get not thy thoUWhts tVoUFGe thee, noV Get thy AoUntenanAe Fe AhanWed; theVe Bs a man Bn thy HBnWdom, Bn Yhom Bs the sQBVBt oI the hoGy Wods; and Bn the days oI thy IatheV GBWht and UndeVstandBnW and YBsdom, GBHe the YBsdom oI the Wods, Yas IoUnd Bn hBm; Yhom the HBnW neFUAhadneOOaV thy IatheV, the HBnW, B say, thy IatheV, made masteV oI the maWBABans, astVoGoWeVs, AhaGdeans, and soothsayeVs; IoVasmUAh as an eZAeGGent sQBVBt, and HnoYGedWe, and UndeVstandBnW, BnteVQVetBnW oI dVeams, and shoYBnW oI haVd sentenAes, and dBssoGDBnW oI doUFts, YeVe IoUnd Bn the same danBeG, Yhom the HBnW named FeGteshaOOaV; noY Get danBeG Fe AaGGed, and he YBGG shoY the BnteVQVetatBon. the IBVst AodeYoVd Bs otheGGo.
```

"sentenAes" implies A is probably c

```
> sub A c
> print current
Bn the same hoUV came IoVth IBnWeVs oI a man’s hand, and YVote oDeV aWaBnst the candGestBcH UQon the QGasteV oI the YaGG oI the HBnW’s QaGace; and the HBnW saY the QaVt oI the hand that YVote. then the HBnW’s coUntenance Yas chanWed, and hBs thoUWhts tVoUFGed hBm, so that the SoBnts oI hBs GoBns YeVe Goosed, and hBs Hnees smote one aWaBnst anotheV. the HBnW cVBed aGoUd to FVBnW Bn the astVoGoWeVs, the chaGdeans, and the soothsayeVs. and the HBnW sQaHe, and saBd to the YBse men oI FaFyGon, YhosoeDeV shaGG Vead thBs YVBtBnW, and shoY me the BnteVQVetatBon theVeoI, shaGG Fe cGothed YBth scaVGet, and haDe a chaBn oI WoGd aFoUt hBs necH, and shaGG Fe the thBVd VUGeV Bn the HBnWdom. then came Bn aGG the HBnW’s YBse men; FUt they coUGd not Vead the YVBtBnW, noV maHe HnoYn to the HBnW the BnteVQVetatBon theVeoI. then Yas HBnW FeGshaOOaV WVeatGy tVoUFGed, and hBs coUntenance Yas chanWed Bn hBm, and hBs GoVds YeVe astonBshed. noY the KUeen, Fy Veason oI the YoVds oI the HBnW and hBs GoVds, came Bnto the FanKUet hoUse; and the KUeen sQaHe and saBd, o HBnW, GBDe IoVeDeV; Get not thy thoUWhts tVoUFGe thee, noV Get thy coUntenance Fe chanWed; theVe Bs a man Bn thy HBnWdom, Bn Yhom Bs the sQBVBt oI the hoGy Wods; and Bn the days oI thy IatheV GBWht and UndeVstandBnW and YBsdom, GBHe the YBsdom oI the Wods, Yas IoUnd Bn hBm; Yhom the HBnW neFUchadneOOaV thy IatheV, the HBnW, B say, thy IatheV, made masteV oI the maWBcBans, astVoGoWeVs, chaGdeans, and soothsayeVs; IoVasmUch as an eZceGGent sQBVBt, and HnoYGedWe, and UndeVstandBnW, BnteVQVetBnW oI dVeams, and shoYBnW oI haVd sentences, and dBssoGDBnW oI doUFts, YeVe IoUnd Bn the same danBeG, Yhom the HBnW named FeGteshaOOaV; noY Get danBeG Fe caGGed, and he YBGG shoY the BnteVQVetatBon. the IBVst codeYoVd Bs otheGGo.
```

codeYoVd is probably codeword

```
> sub Y w
> sub V r
> print current
Bn the same hoUr came Iorth IBnWers oI a man’s hand, and wrote oDer aWaBnst the candGestBcH UQon the QGaster oI the waGG oI the HBnW’s QaGace; and the HBnW saw the Qart oI the hand that wrote. then the HBnW’s coUntenance was chanWed, and hBs thoUWhts troUFGed hBm, so that the SoBnts oI hBs GoBns were Goosed, and hBs Hnees smote one aWaBnst another. the HBnW crBed aGoUd to FrBnW Bn the astroGoWers, the chaGdeans, and the soothsayers. and the HBnW sQaHe, and saBd to the wBse men oI FaFyGon, whosoeDer shaGG read thBs wrBtBnW, and show me the BnterQretatBon thereoI, shaGG Fe cGothed wBth scarGet, and haDe a chaBn oI WoGd aFoUt hBs necH, and shaGG Fe the thBrd rUGer Bn the HBnWdom. then came Bn aGG the HBnW’s wBse men; FUt they coUGd not read the wrBtBnW, nor maHe Hnown to the HBnW the BnterQretatBon thereoI. then was HBnW FeGshaOOar WreatGy troUFGed, and hBs coUntenance was chanWed Bn hBm, and hBs Gords were astonBshed. now the KUeen, Fy reason oI the words oI the HBnW and hBs Gords, came Bnto the FanKUet hoUse; and the KUeen sQaHe and saBd, o HBnW, GBDe IoreDer; Get not thy thoUWhts troUFGe thee, nor Get thy coUntenance Fe chanWed; there Bs a man Bn thy HBnWdom, Bn whom Bs the sQBrBt oI the hoGy Wods; and Bn the days oI thy Iather GBWht and UnderstandBnW and wBsdom, GBHe the wBsdom oI the Wods, was IoUnd Bn hBm; whom the HBnW neFUchadneOOar thy Iather, the HBnW, B say, thy Iather, made master oI the maWBcBans, astroGoWers, chaGdeans, and soothsayers; IorasmUch as an eZceGGent sQBrBt, and HnowGedWe, and UnderstandBnW, BnterQretBnW oI dreams, and showBnW oI hard sentences, and dBssoGDBnW oI doUFts, were IoUnd Bn the same danBeG, whom the HBnW named FeGteshaOOar; now Get danBeG Fe caGGed, and he wBGG show the BnterQretatBon. the IBrst codeword Bs otheGGo.
```

Iorth

I is probably f.  Though the word would be 'worth' potentially, it comes after the word 'came' so it probably is an 'f'.

```
> sub I f
> print current
Bn the same hoUr came forth fBnWers of a man’s hand, and wrote oDer aWaBnst the candGestBcH UQon the QGaster of the waGG of the HBnW’s QaGace; and the HBnW saw the Qart of the hand that wrote. then the HBnW’s coUntenance was chanWed, and hBs thoUWhts troUFGed hBm, so that the SoBnts of hBs GoBns were Goosed, and hBs Hnees smote one aWaBnst another. the HBnW crBed aGoUd to FrBnW Bn the astroGoWers, the chaGdeans, and the soothsayers. and the HBnW sQaHe, and saBd to the wBse men of FaFyGon, whosoeDer shaGG read thBs wrBtBnW, and show me the BnterQretatBon thereof, shaGG Fe cGothed wBth scarGet, and haDe a chaBn of WoGd aFoUt hBs necH, and shaGG Fe the thBrd rUGer Bn the HBnWdom. then came Bn aGG the HBnW’s wBse men; FUt they coUGd not read the wrBtBnW, nor maHe Hnown to the HBnW the BnterQretatBon thereof. then was HBnW FeGshaOOar WreatGy troUFGed, and hBs coUntenance was chanWed Bn hBm, and hBs Gords were astonBshed. now the KUeen, Fy reason of the words of the HBnW and hBs Gords, came Bnto the FanKUet hoUse; and the KUeen sQaHe and saBd, o HBnW, GBDe foreDer; Get not thy thoUWhts troUFGe thee, nor Get thy coUntenance Fe chanWed; there Bs a man Bn thy HBnWdom, Bn whom Bs the sQBrBt of the hoGy Wods; and Bn the days of thy father GBWht and UnderstandBnW and wBsdom, GBHe the wBsdom of the Wods, was foUnd Bn hBm; whom the HBnW neFUchadneOOar thy father, the HBnW, B say, thy father, made master of the maWBcBans, astroGoWers, chaGdeans, and soothsayers; forasmUch as an eZceGGent sQBrBt, and HnowGedWe, and UnderstandBnW, BnterQretBnW of dreams, and showBnW of hard sentences, and dBssoGDBnW of doUFts, were foUnd Bn the same danBeG, whom the HBnW named FeGteshaOOar; now Get danBeG Fe caGGed, and he wBGG show the BnterQretatBon. the fBrst codeword Bs otheGGo.
```

aWaBnst probably against

```
> sub W g
> sub B i
> print current
in the same hoUr came forth fingers of a man’s hand, and wrote oDer against the candGesticH UQon the QGaster of the waGG of the Hing’s QaGace; and the Hing saw the Qart of the hand that wrote. then the Hing’s coUntenance was changed, and his thoUghts troUFGed him, so that the Soints of his Goins were Goosed, and his Hnees smote one against another. the Hing cried aGoUd to Fring in the astroGogers, the chaGdeans, and the soothsayers. and the Hing sQaHe, and said to the wise men of FaFyGon, whosoeDer shaGG read this writing, and show me the interQretation thereof, shaGG Fe cGothed with scarGet, and haDe a chain of goGd aFoUt his necH, and shaGG Fe the third rUGer in the Hingdom. then came in aGG the Hing’s wise men; FUt they coUGd not read the writing, nor maHe Hnown to the Hing the interQretation thereof. then was Hing FeGshaOOar greatGy troUFGed, and his coUntenance was changed in him, and his Gords were astonished. now the KUeen, Fy reason of the words of the Hing and his Gords, came into the FanKUet hoUse; and the KUeen sQaHe and said, o Hing, GiDe foreDer; Get not thy thoUghts troUFGe thee, nor Get thy coUntenance Fe changed; there is a man in thy Hingdom, in whom is the sQirit of the hoGy gods; and in the days of thy father Gight and Understanding and wisdom, GiHe the wisdom of the gods, was foUnd in him; whom the Hing neFUchadneOOar thy father, the Hing, i say, thy father, made master of the magicians, astroGogers, chaGdeans, and soothsayers; forasmUch as an eZceGGent sQirit, and HnowGedge, and Understanding, interQreting of dreams, and showing of hard sentences, and dissoGDing of doUFts, were foUnd in the same danieG, whom the Hing named FeGteshaOOar; now Get danieG Fe caGGed, and he wiGG show the interQretation. the first codeword is otheGGo.
```

candGesticH is candlestick

```
> sub G l
> sub H k
> print current
in the same hoUr came forth fingers of a man’s hand, and wrote oDer against the candlestick UQon the Qlaster of the wall of the king’s Qalace; and the king saw the Qart of the hand that wrote. then the king’s coUntenance was changed, and his thoUghts troUFled him, so that the Soints of his loins were loosed, and his knees smote one against another. the king cried aloUd to Fring in the astrologers, the chaldeans, and the soothsayers. and the king sQake, and said to the wise men of FaFylon, whosoeDer shall read this writing, and show me the interQretation thereof, shall Fe clothed with scarlet, and haDe a chain of gold aFoUt his neck, and shall Fe the third rUler in the kingdom. then came in all the king’s wise men; FUt they coUld not read the writing, nor make known to the king the interQretation thereof. then was king FelshaOOar greatly troUFled, and his coUntenance was changed in him, and his lords were astonished. now the KUeen, Fy reason of the words of the king and his lords, came into the FanKUet hoUse; and the KUeen sQake and said, o king, liDe foreDer; let not thy thoUghts troUFle thee, nor let thy coUntenance Fe changed; there is a man in thy kingdom, in whom is the sQirit of the holy gods; and in the days of thy father light and Understanding and wisdom, like the wisdom of the gods, was foUnd in him; whom the king neFUchadneOOar thy father, the king, i say, thy father, made master of the magicians, astrologers, chaldeans, and soothsayers; forasmUch as an eZcellent sQirit, and knowledge, and Understanding, interQreting of dreams, and showing of hard sentences, and dissolDing of doUFts, were foUnd in the same daniel, whom the king named FelteshaOOar; now let daniel Fe called, and he will show the interQretation. the first codeword is othello.
```

we could go on, but we can now see the last sentence:

the first codeword is othello.

Congratulations!  We deciphered Billy's message!