<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:math="http://www.w3.org/2005/xpath-functions/math"
    exclude-result-prefixes="xs math"
    version="3.0">
 
    <xsl:output method="text" indent="no"/>
    
    <xsl:variable name="collection" as="document-node()+" select="collection('xml-markup2/?select=*.xml')"/>
    
    <xsl:variable name="distinctChars" as="xs:string+" select="$collection//character 
        ! normalize-space()
        ! upper-case(.) 
        => distinct-values()"/>
    
    <xsl:variable name="tab" as="xs:string">
        <xsl:text>&#x9;</xsl:text>
    </xsl:variable>
    
    <xsl:variable name="newline" as="xs:string">
        <xsl:text>&#10;</xsl:text>
    </xsl:variable>
    
    <xsl:template match="/">
        <!-- These are titles for the columns -->
        <xsl:text>Character(s)</xsl:text>
        <xsl:value-of select="$tab"/>
        <xsl:text>SpeechPerEpisode</xsl:text>
        <xsl:value-of select="$tab"/>
        <xsl:text>Episode #</xsl:text>
        <xsl:value-of select="$newline"/>
       
        <xsl:for-each select="$distinctChars">
            <xsl:variable name="currentChar" as="xs:string" select="current()"/>
           
            <xsl:for-each select="$collection">
                <xsl:variable name="countSpeeches" as="xs:integer" 
                    select="current()//character[.
                    ! normalize-space()
                    ! upper-case(.) = $currentChar] => count()"/>
                
               <xsl:if test="$countSpeeches &gt; 0"> 
                   
                   <xsl:value-of select="$currentChar"/>
                
                <xsl:value-of select="$tab"/>
               
                <xsl:value-of select="$countSpeeches"/>
                <xsl:value-of select="$tab"/>
                
                <xsl:value-of select="current() ! base-uri() ! tokenize(., '/')[last()] "/>
                
                <xsl:value-of select="$newline"/></xsl:if>
          
            </xsl:for-each>
           
            
            
        </xsl:for-each>

     
    </xsl:template>
    
  
</xsl:stylesheet>