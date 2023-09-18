import React, { Component } from "react";
import Dashboard from "./Dashboard";



export default class HomePage extends Component {
  constructor(props) {
    super(props);
  }
  
  render() {
    return (
        <div>
          <section id="hero" class="d-flex justify-cntent-center align-items-center">
            <div id="heroCarousel" class="container carousel carousel-fade" data-bs-ride="carousel" data-bs-interval="5000">
                <div class="carousel-item active">
                    <div class="carousel-container">
                    <h2 class="animate__animated animate__fadeInDown">Welcome to <span>the DGI Portal</span></h2>
                    <p class="animate__animated animate__fadeInUp">Optimisez l'Analyse des Revenus Fiscaux pour le Ministère de l'Économie et des Finances, DGI Portal représente une percée majeure pour les cadres du Ministère de l'Économie et des Finances, mettant à leur disposition un outil novateur pour étudier en profondeur les revenus des impôts. Notre plateforme offre une interface conviviale spécifiquement conçue pour répondre aux besoins complexes de l'administration fiscale, permettant une analyse approfondie des données fiscales en temps réel.</p>
                    <a href="/api/dashboard" class="btn-get-started animate__animated animate__fadeInUp">Go to Dashboard</a>
                    </div>
                </div>
                <div class="carousel-item">
                    <div class="carousel-container">
                    <h2 class="animate__animated animate__fadeInDown">L'Intelligence Artificielle au Service de l'Analyse Fiscale</h2>  
                    <p class="animate__animated animate__fadeInUp">DGI Portal intègre une puissante technologie d'Intelligence Artificielle (IA) qui simplifie le processus d'analyse des revenus fiscaux. Grâce à des algorithmes avancés de traitement du langage naturel (NLP) et d'analyse de données, notre plateforme extrait automatiquement des informations cruciales des déclarations fiscales, identifie les tendances fiscales émergentes, et génère des rapports détaillés en temps réel. Les cadres du ministère peuvent ainsi prendre des décisions informées pour optimiser la collecte des impôts.</p>
                    <a href="/api/dashboard" class="btn-get-started animate__animated animate__fadeInUp">Go to Dashboard</a>
                    </div>
                </div>
                <div class="carousel-item">
                    <div class="carousel-container">
                    <h2 class="animate__animated animate__fadeInDown">Un Partenaire Essentiel pour une Gestion Fiscale Efficace</h2>
                    <p class="animate__animated animate__fadeInUp">DGI Portal est bien plus qu'une simple plateforme, c'est un partenaire essentiel pour le Ministère de l'Économie et des Finances dans sa mission de gestion fiscale. Notre solution révolutionnaire simplifie la gestion des revenus fiscaux, augmente l'efficacité des processus et améliore la prise de décision stratégique. Grâce à DGI Portal, les cadres du ministère disposent d'un outil puissant pour garantir une collecte de revenus fiscaux plus efficace et une meilleure gestion des finances publiques. Découvrez comment DGI Portal peut transformer la gestion fiscale au Ministère de l'Économie et des Finances dès aujourd'hui.</p>
                    <a href="/api/dashboard" class="btn-get-started animate__animated animate__fadeInUp">Go to Dashboard</a>
                    </div>
                </div>
                <a class="carousel-control-prev" href="#heroCarousel" role="button" data-bs-slide="prev">
                    <span class="carousel-control-prev-icon bx bx-chevron-left" aria-hidden="true"></span>
                </a>
                <a class="carousel-control-next" href="#heroCarousel" role="button" data-bs-slide="next">
                    <span class="carousel-control-next-icon bx bx-chevron-right" aria-hidden="true"></span>
                </a>

            </div>
          </section>
          <main id="main">
            <section class="services">
                <div class="container">
                    <div class="row">
                        <div class="col-md-6 col-lg-3 d-flex align-items-stretch" data-aos="fade-up">
                            <div class="icon-box icon-box-pink">
                            <div class="icon"><i class="bx bxl-dribbble"></i></div>
                            <h4 class="title"><a href="chiffresCle.html">Chiffres clés</a></h4>
                            <p class="description">Voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi sint occaecati cupiditate non provident</p>
                            </div>
                        </div>

                        <div class="col-md-6 col-lg-3 d-flex align-items-stretch" data-aos="fade-up" data-aos-delay="100">
                            <div class="icon-box icon-box-cyan">
                            <div class="icon"><i class="bx bx-file"></i></div>
                            <h4 class="title"><a href="Ratio.html">Ratios</a></h4>
                            <p class="description">Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur</p>
                            </div>
                        </div>

                        <div class="col-md-6 col-lg-3 d-flex align-items-stretch" data-aos="fade-up" data-aos-delay="200">
                            <div class="icon-box icon-box-green">
                            <div class="icon"><i class="bx bx-tachometer"></i></div>
                            <h4 class="title"><a href="Dividend.html">Dividend</a></h4>
                            <p class="description">Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum</p>
                            </div>
                        </div>

                        <div class="col-md-6 col-lg-3 d-flex align-items-stretch" data-aos="fade-up" data-aos-delay="200">
                            <div class="icon-box icon-box-blue">
                            <div class="icon"><i class="bx bx-world"></i></div>
                            <h4 class="title"><a href="Retourner.html">Retourner</a></h4>
                            <p class="description">At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque</p>
                            </div>
                        </div>

                    </div>

                </div>
            </section>
        </main>
        <a href="#" class="back-to-top d-flex align-items-center justify-content-center"><i class="bi bi-arrow-up-short"></i></a>
      </div>
    );
  }
}











