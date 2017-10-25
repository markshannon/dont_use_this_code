
class DerivedTrustManager(BaseTrustManager):
    
    def checkServerTrusted(self, chain, auth_type):
        for trust_manager in self.trust_managers:
            try:
                trustManager.checkServerTrusted(chain, auth_type);
                return
            except CertificateException:
                pass

        raise CertificateException("None of the TrustManagers trust this certificate chain")
